from pydantic import BaseModel, ConfigDict


class GetBotGroupsRequest(BaseModel):
    model_config = ConfigDict(extra='forbid')

    name: str | None = None
    exchange: str | None = None
    is_active: bool | None = None
