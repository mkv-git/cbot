from typing import Any


def get_positions(params: dict[str, Any]) -> str:
    query = """
        SELECT *
        FROM positions
        WHERE 1=1
    """

    for p in params.keys():
        query += f" AND {p} = %({p})s "

    return query
