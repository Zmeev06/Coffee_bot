import aiomysql
from aiomysql import cursors

from tgbot.database import connect, close_connection


async def new_use (connection: aiomysql.Connection, user_id):
    cursor = await connection.cursor()
    await cursor.execute('SELECT id FROM users WHERE user_id=%s', (user_id))
    id = await cursor.fetchone()
    if id is not None:
        return 1
    else:
        return 0
