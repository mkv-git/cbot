from typing import Any, Type

from loguru import logger
from pydantic import ValidationError

from cbot.utils.classifiers import REQ, RESP, MODEL


def validate(model: Type[MODEL], params: Any) -> MODEL:
    return model.model_validate(params)
