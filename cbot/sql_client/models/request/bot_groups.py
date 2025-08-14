from pydantic import BaseModel, ConfigDict


class GetBotGroupByIdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bot_group_id: int


class GetBotGroupsRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str | None = None
    exchange: str | None = None
    is_active: bool | None = None


class GetBotGroupsConfigRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bot_group_id: int


class GetBotGroupsSecretsRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bot_group_id: int
    is_active: bool | None = None
