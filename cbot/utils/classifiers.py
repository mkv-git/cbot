from enum import StrEnum
from typing import Generic, TypeVar

from pydantic import BaseModel

REQ = TypeVar("REQ", bound=BaseModel)
RESP = TypeVar("RESP", bound=BaseModel)
MODEL = TypeVar("MODEL", bound=BaseModel)


class ResponseStatus(StrEnum):
    ERROR = "error"
    SUCCESS = "success"
