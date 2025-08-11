from pydantic import BaseModel, RootModel, Field

class QueryResponseData(BaseModel):
    id: int
    bot_group_id: int
    token: str
    order_name: str
    leverage: int


GetPositionsResponse = RootModel[list[QueryResponseData]]
