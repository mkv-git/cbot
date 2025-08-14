from enum import StrEnum
from typing import TypeVar, Any

from pydantic import BaseModel

type TDictAny = dict[str, Any]

REQ = TypeVar("REQ", bound=BaseModel)
RESP = TypeVar("RESP", bound=BaseModel)
MODEL = TypeVar("MODEL", bound=BaseModel)


class ResponseStatus(StrEnum):
    ERROR = "error"
    SUCCESS = "success"
