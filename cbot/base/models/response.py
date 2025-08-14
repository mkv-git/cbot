from pydantic import BaseModel

from cbot.utils.classifiers import ResponseStatus, TDictAny


class WSResponse(BaseModel):
    status: ResponseStatus
    result: list[TDictAny] | str
