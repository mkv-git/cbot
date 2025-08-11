import os
from typing import Type

from loguru import logger
from psycopg_pool import AsyncConnectionPool


def get_url() -> str:
    return "postgresql://%s:%s@%s:%s/%s" % (
        os.getenv("CBOT_DB_USERNAME"),
        os.getenv("CBOT_DB_PASSWORD"),
        os.getenv("CBOT_DB_HOST"),
        os.getenv("CBOT_DB_PORT"),
        os.getenv("CBOT_DB_NAME"),
    )


class DataBase:
    pool: AsyncConnectionPool | None = None


db = DataBase()


async def get_database():
    if db.pool is None:
        await reconnect_db()

    return db


async def reconnect_db():
    logger.info("Reconnecting to database")

    try:
        db.pool = AsyncConnectionPool(get_url(), open=False)
        await db.pool.open(wait=False)
        logger.info("DB reconnected")
    except Exception as err:
        logger.error(f"Reconnecting failed: {err}")
