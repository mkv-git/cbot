from typing import Any

from cbot.sql_client.queries.positions import get_positions
from cbot.sql_client.models.request.positions import GetPositionsRequest

from cbot.sql_client.queries.bot_groups import (
    get_bot_groups,
    get_bot_group_by_id,
    get_bot_group_config,
    get_bot_group_secrets,
)
from cbot.sql_client.models.request.bot_groups import (
    GetBotGroupByIdRequest,
    GetBotGroupsRequest,
    GetBotGroupsConfigRequest,
    GetBotGroupsSecretsRequest,
)


sql_registry: dict[str, Any] = {
    "get_positions": {
        "query_str": get_positions,
        "request_model": GetPositionsRequest,
    },
    "get_bot_groups": {
        "query_str": get_bot_groups,
        "request_model": GetBotGroupsRequest,
    },
    "get_bot_group_by_id": {
        "query_str": get_bot_group_by_id,
        "request_model": GetBotGroupByIdRequest,
    },
    "get_bot_group_config": {
        "query_str": get_bot_group_config,
        "request_model": GetBotGroupsConfigRequest,
    },
    "get_bot_group_secrets": {
        "query_str": get_bot_group_secrets,
        "request_model": GetBotGroupsSecretsRequest,
    },
}
