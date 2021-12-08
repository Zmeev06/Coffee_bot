import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ParseMode, chat, message
from aiogram.utils import callback_data
from aiogram.utils.exceptions import MessageNotModified
import aiogram.utils.markdown as fmt
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.utils.mixins import T
from aiomysql import connection
from tgbot import config

from . import keyboards
from . import dbworker


from tgbot.database import connect, close_connection
from load_all import bot


class New_user (StatesGroup):
    name = State()
    second_name = State()
    age = State()

async def new_user_name (call:types.CallbackQuery):
    await call.message.reply(
        text='Перед началом стажировки нужно указать некоторые данные.\
            \n\nУкажите ваше имя.',
        disable_web_page_preview=True,
        reply=False
    )
    await call.answer()
    await New_user.name.set()


async def new_user_second_name (message:types.Message, state:FSMContext):
    name = message.text
    con = await connect()
    user_id = message.from_user.id
    await dbworker.users_name(con, name, user_id)
    await dbworker.new_user_name(con, name, user_id)
    await close_connection(con)

    await message.answer('Отлично, теперь укажи свою фамилию')

    await New_user.second_name.set()


async def set_age (message:types.Message, state:FSMContext):
    second_name = message.text
    con = await connect()
    user_id = message.from_user.id
    await dbworker.users_second_name(con, second_name, user_id)
    await dbworker.new_user_second_name(con, second_name, user_id)
    await close_connection(con)

    await message.answer('Сколько вам лет?')
    await New_user.age.set()


async def experience (message: types.Message, state:FSMContext):
    age = int(message.text)
    user_id = message.from_user.id
    con = await connect()
    await dbworker.age(con, age, user_id)

    await message.reply(
        text='У вас есть опыт работы?',
        reply_markup=await keyboards.exp(),
        reply=False,
        disable_web_page_preview=True
    )
    await close_connection(con)
    await state.finish()


def new_user_register(dp:Dispatcher):
    dp.register_callback_query_handler(new_user_name, text='start_new_user')
    dp.register_message_handler(new_user_second_name, state=New_user.name)
    dp.register_message_handler(set_age, state=New_user.second_name)
    dp.register_message_handler(experience, state=New_user.age)
