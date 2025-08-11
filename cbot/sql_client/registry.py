from typing import Any

from cbot.sql_client.queries.get_positions import get_positions
from cbot.sql_client.models.request.get_positions import GetPositionsRequest
from cbot.sql_client.models.response.get_positions import GetPositionsResponse

from cbot.sql_client.queries.get_bot_groups import get_bot_groups
from cbot.sql_client.models.request.get_bot_groups import GetBotGroupsRequest
from cbot.sql_client.models.response.get_bot_groups import GetBotGroupsResponse


sql_registry: dict[str, Any] = {
    "get_positions": {
        "query_str": get_positions,
        "request_model": GetPositionsRequest,
        "response_model": GetPositionsResponse,
    },
    "get_bot_groups": {
        "query_str": get_bot_groups,
        "request_model": GetBotGroupsRequest,
        "response_model": GetBotGroupsResponse,
    },
}
