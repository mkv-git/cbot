from typing import Generic

from pydantic import BaseModel

from cbot.utils.classifiers import RESP, ResponseStatus


class ErrorResponse(BaseModel):
    result: str


class WSResponse(BaseModel, Generic[RESP]):
    status: ResponseStatus
    data: RESP | ErrorResponse
