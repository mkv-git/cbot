from typing import Any

from cbot.utils.classifiers import TDictAny

def get_bot_group_by_id(params: TDictAny) -> str:
    query = """
        SELECT
            bg.group_name, bg.uid, bg.exchange,
            bgc.public_ws_port, bgc.private_ws_port, bgc.trade_ws_port, bgc.rest_api_ws_port
        FROM bot_groups AS bg
        JOIN bot_group_config AS bgc ON bg.id = bgc.bot_group_id
        WHERE bg.id = %(bot_group_id)s
            AND bg.is_active = True
        LIMIT 1
    """

    return query


def get_bot_groups(params: TDictAny) -> str:
    query = """
        SELECT *
        FROM bot_groups
        WHERE 1=1
    """

    for p in params.keys():
        query += f" AND {p} = %({p})s "

    return query


def get_bot_group_config(params: TDictAny) -> str:
    query = """
        SELECT *
        FROM bot_group_config
        WHERE bot_group_id = %(bot_group_id)s
    """

    return query


def get_bot_group_secrets(params: TDictAny) -> str:
    query = """
        SELECT *
        FROM bot_group_secrets
        WHERE bot_group_id = %(bot_group_id)s
    """
    for p in params.keys():
        query += f" AND {p} = %({p})s "

    return query
