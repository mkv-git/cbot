from pydantic import BaseModel, ConfigDict


class GetPositionsRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    order_name: str | None = None
    is_active: bool | None = None
    bot_group_id: int | None = None
