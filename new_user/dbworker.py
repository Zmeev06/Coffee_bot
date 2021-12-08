import aiomysql
from aiomysql import cursors

from tgbot.database import connect, close_connection


async def users_name(connection: aiomysql.Connection, name, user_id):
    cursor = await connection.cursor()
    await cursor.execute('SELECT name FROM users WHERE user_id=%s', (user_id))
    if await cursor.fetchone() is None:
        await cursor.execute('INSERT INTO users (user_id, name) VALUES (%s, %s)', (user_id, name))
    await connection.commit()
    
async def new_user_name (connection: aiomysql.Connection, name, user_id):
    cursor = await connection.cursor()
    await cursor.execute('SELECT id FROM users WHERE user_id=%s', (user_id))
    id = await cursor.fetchone()
    id = id.get('id')

    await cursor.execute('INSERT INTO new_users (id) VALUES (%s)', (id))
    await cursor.execute('UPDATE new_users SET name=%s WHERE id = %s', (name, id))
    await cursor.execute('UPDATE new_users SET user_id = %s WHERE id=%s', (user_id, id))
    await connection.commit()

    
async def new_use (connection: aiomysql.Connection, user_id):
    cursor = await connection.cursor()
    await cursor.execute('SELECT id FROM users WHERE user_id=%s', (user_id))
    id = await cursor.fetchall()
    if id is not None:
        return 1
    else:
        return 0


async def users_second_name (connection: aiomysql.Connection, second_name, user_id):
    cursor = await connection.cursor()
    await cursor.execute('SELECT second_name FROM users WHERE user_id=%s', (user_id))
    i = await cursor.fetchone()
    if i.get('second_name') == None:
        await cursor.execute('UPDATE users SET second_name=%s WHERE user_id=%s', (second_name, user_id))
    await connection.commit()

async def new_user_second_name(connection: aiomysql.Connection, second_name, user_id):
    cursor = await connection.cursor()
    await cursor.execute('SELECT id FROM users WHERE user_id=%s', (user_id))
    id = await cursor.fetchone()
    id = id.get('id')
    
    await cursor.execute('UPDATE new_users SET second_name=%s WHERE id = %s', (second_name, id))
    await connection.commit()


async def age (connection: aiomysql.Connection, age, user_id):
    cursor = await connection.cursor()

    await cursor.execute('UPDATE new_users SET age=%s WHERE user_id=%s', (age,user_id))

    await connection.commit()