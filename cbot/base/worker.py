import os
import asyncio
from pprint import pprint
from typing import Generic, Any
from abc import ABC, abstractmethod

import zmq
import ujson
from loguru import logger
from pydantic import ValidationError
from overrides import final, EnforceOverrides
from zmq.asyncio import Context, Socket, Poller

from cbot.base.models.request import WSRequest
from cbot.utils.classifiers import REQ, RESP, MODEL, ResponseStatus
from cbot.base.models.response import WSResponse, ErrorResponse
from cbot.config.const import (
    INPROC_BACKEND_ADDR,
    LOGGING_FILE_ROOT_DIR,
    DEFAULT_WS_REQUEST_RETRIES,
    DEFAULT_WS_REQUEST_TIMEOUT,
    DEFAULT_LOGGING_FILE_CONFIG,
)


class AbstractBaseWorker(ABC, Generic[REQ, RESP], EnforceOverrides):
    WORKER: str = "NOTSET"

    def __init__(self):
        self.WORKER = self.__class__.__name__
        self.tasks = []
        self.context = Context()
        self.setup_logger()
        self.set_shell_title()

    def setup_logger(self):
        logger.remove(0)
        file_path = f"{LOGGING_FILE_ROOT_DIR}/{self.WORKER}/main_{{time:DD-MM-YYYY}}.log"
        logger.add(file_path, **DEFAULT_LOGGING_FILE_CONFIG)

    def set_shell_title(self, title: str | None = None):
        shell_title = title if title else self.WORKER
        os.system(f'echo "\033]0;{shell_title}\a"')

    @abstractmethod
    async def run(self):
        pass

    @abstractmethod
    async def setup_socks_vault(self):
        pass

    @final
    async def handle_success(self, payload: Any) -> WSResponse[RESP]:
        return WSResponse(status=ResponseStatus.SUCCESS, data=payload)

    @final
    async def handle_error(self, msg: str) -> WSResponse[RESP]:
        return WSResponse(status=ResponseStatus.ERROR, data=ErrorResponse(result=msg))

    async def worker_query(self, payload: list[Any], sock_item: dict[str, Any]):
        sock_obj = sock_item["obj"]
        sock_name = list(sock_item.keys())[0]
        await sock_obj.send_multipart(payload)

        retries_left = DEFAULT_WS_REQUEST_RETRIES
        while 1:
            if (await sock_obj.poll(DEFAULT_WS_REQUEST_TIMEOUT) & zmq.POLLIN) != 0:
                msg = await sock_obj.recv_multipart()
                return msg

            retries_left -= 1
            logger.warning(f"No response from worker({sock_name})")
            sock_obj.setsockopt(zmq.LINGER, 0)
            sock_obj.close()

            if retries_left == 0:
                logger.error(f"Worker({sock_name}) offline, abort!")
                sock_item["obj"] = None
                return

            logger.info(f"Reconnecting to worker({sock_name})")
            sock_item["obj"] = sock_obj = self.context.socket(zmq.DEALER)
            sock_obj.connect(sock_item["connection"])
            logger.info(f"Resending {payload}")
            await sock_obj.send_multipart(payload)

    async def req_rep_proxy(self, context: Context, worker_port: int):
        frontend = context.socket(zmq.ROUTER)
        frontend.bind(f"tcp://*:{worker_port}")

        backend = context.socket(zmq.DEALER)
        backend.bind(INPROC_BACKEND_ADDR)

        poller = Poller()
        poller.register(frontend, zmq.POLLIN)
        poller.register(backend, zmq.POLLIN)

        while 1:
            poll_events = await poller.poll()
            events = dict(poll_events)

            if frontend in events:
                msg = await frontend.recv_multipart(copy=False)
                await backend.send_multipart(msg)
            elif backend in events:
                msg = await backend.recv_multipart(copy=False)
                await frontend.send_multipart(msg)

        await frontend.close()
        await backend.close()
