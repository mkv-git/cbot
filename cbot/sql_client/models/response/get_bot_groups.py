from pydantic import BaseModel, RootModel, Field


class QueryResponseData(BaseModel):
    name: str = Field(alias='group_name')
    uid: int
    exchange: str


GetBotGroupsResponse = RootModel[list[QueryResponseData]]
