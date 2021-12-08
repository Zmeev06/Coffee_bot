import logging

import asyncio
import aiomysql
from aiomysql.cursors import DictCursor


from .config import load_config

logger = logging.getLogger(__name__)

config = load_config('bot.ini')


async def connect() -> aiomysql.Connection:
    
    try:
        return await aiomysql.connect(
            user=config.db.user,
            password=config.db.password,
            db=config.db.database,
            host=config.db.host,
            charset='utf8mb4',
            cursorclass=DictCursor,
        )
    except Exception as e:
        logger.exception('error when connection to DB:', e)
        raise NotImplementedError
        

async def close_connection(connection: aiomysql.Connection):
    await connection.commit()
    return connection.close()