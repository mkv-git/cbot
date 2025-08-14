from pydantic import BaseModel, RootModel, Field


class QueryResponseData(BaseModel):
    id: int
    trade_ws_port: int
    public_ws_port: int
    private_ws_port: int
    rest_api_ws_port: int


GetBotGroupsConfigResponse = RootModel[list[QueryResponseData]]
