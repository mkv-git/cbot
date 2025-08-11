from typing import Any


def get_bot_groups(params: dict[str, Any]) -> str:
    query = """
        SELECT *
        FROM bot_groups
        WHERE 1=1
    """

    for p in params.keys():
        query += f" AND {p} = %({p})s "

    return query
