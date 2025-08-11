import os
import random
import asyncio
from typing import Any

import zmq
import ujson
from loguru import logger
from overrides import override
from psycopg.rows import dict_row
from pydantic import ValidationError
from zmq.asyncio import Context, Poller

from cbot.utils.validation import validate
from cbot.utils.classifiers import REQ, RESP, MODEL
from cbot.base.worker import AbstractBaseWorker

from cbot.sql_client.database import get_database

from cbot.sql_client.registry import sql_registry
from cbot.config.const import SQL_WORKER_PORT, INPROC_BACKEND_ADDR, DEFAULT_LOGGING_FILE_CONFIG

DEFAULT_WORKER_CNT = 5


class SqlWorker(AbstractBaseWorker[REQ, RESP]):

    @override
    async def run(self):
        logger.info(f"{self.WORKER} started")

        self.tasks.append(self.req_rep_proxy(self.context, SQL_WORKER_PORT))

        for _ in range(DEFAULT_WORKER_CNT):
            self.tasks.append(self.worker(self.context))

        await asyncio.gather(*self.tasks)

        logger.info(f"{self.WORKER} finished.")

    @override
    async def setup_socks_vault(self):
        """won't need with this worker, as it won't communicate with other workers"""

        pass

    async def worker(self, context: Context):
        obj = context.socket(zmq.DEALER)
        obj.connect(INPROC_BACKEND_ADDR)

        while 1:
            ident, *payload = await obj.recv_multipart()
            res = await self.process(payload)
            await obj.send_multipart([ident, ujson.dumps(res.model_dump()).encode("ascii")])

        await obj.close()

    async def process(self, in_val: list[Any]):
        try:
            process_name, *raw_process_params = in_val
            process_name = process_name.decode("ascii")
            process_params = ujson.loads(raw_process_params[0].decode("ascii"))

            reg_obj = sql_registry[process_name]
            if process_params:
                req_model = validate(reg_obj["request_model"], process_params)
                query_params = req_model.model_dump(exclude_unset=True)
            else:
                query_params = {}

            query_str: str = reg_obj["query_str"](query_params)
            query_res = await self.make_db_request(query_str, query_params)
            resp_obj = validate(reg_obj["response_model"], query_res)
            return await self.handle_success(resp_obj)
        except KeyError as err:
            err_msg = f'No registry object with name: "{process_name}"'
            return await self.handle_error(err_msg)
        except ValidationError as err:
            logger.warning(err.json())
            err_obj = ujson.loads(err.json())
            err_msg = ujson.dumps({".".join(map(lambda x: str(x), eo["loc"])): eo["msg"] for eo in err_obj})
            return await self.handle_error(err_msg)
        except ValueError as err:
            logger.exception(err)
            return await self.handle_error(str(err))
        except Exception as exc:
            logger.exception(exc)
            return await self.handle_error(f"Unexpected {exc=}")

    async def make_db_request(
        self, query_str: str, params: dict[str, Any] | None
    ) -> list[dict[str, Any]]:
        db = await get_database()
        async with db.pool.connection() as conn:
            async with conn.cursor(row_factory=dict_row) as cursor:
                await cursor.execute(query_str, params)
                res = await cursor.fetchall()

        return res


if __name__ == "__main__":
    asyncio.run(SqlWorker().run())
