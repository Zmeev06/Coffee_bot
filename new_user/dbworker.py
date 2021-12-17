import aiomysql
from aiomysql import cursors
from aiomysql.connection import Connection

from tgbot.database import connect, close_connection

    
async def new_use (connection: aiomysql.Connection, user_id):
    cursor = await connection.cursor()
    await cursor.execute('SELECT id FROM users WHERE user_id=%s', (user_id))
    id = await cursor.fetchall()
    if id is not None:
        return 1
    else:
        return 0

async def new_user(connection: aiomysql.Connection, user_id, name, second_name, age):
    cursor =await connection.cursor()
    is_employer, exp, empl, is_complete = 0,0,0,0
    shifts = 'no'
    await cursor.execute('INSERT INTO users (user_id, name, second_name, age, is_employer, employer) VALUES (%s, %s, %s, %s, %s, %s)',
    (user_id, name, second_name, age, is_employer, empl))
    await connection.commit()
    await cursor.execute('SELECT id FROM users WHERE user_id=%s', (user_id))
    id = await cursor.fetchone()
    id = id['id']
    await cursor.execute('INSERT INTO new_users (id, user_id, name, second_name, shifts, age, experience, employer, is_complete) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
    (id, user_id, name, second_name, shifts, age, exp, empl, is_complete))

    await connection.commit()

async def exp(connection:  aiomysql.Connection, exp, user_id):
    cursor : aiomysql.Connection.cursor
    cursor = await connection.cursor()

    await cursor.execute("UPDATE new_users SET experience = %s WHERE user_id = %s", (exp, user_id))
    await connection.commit()


async def shifts(connection:  aiomysql.Connection, shifts, user_id):
    cursor : aiomysql.Connection.cursor
    cursor = await connection.cursor()

    await cursor.execute("UPDATE new_users SET shifts = %s WHERE user_id = %s", (shifts, user_id))
    await connection.commit()