import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ParseMode, chat, message
from aiogram.utils import callback_data
from aiogram.utils.exceptions import MessageNotModified
import aiogram.utils.markdown as fmt
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text, CommandStart
from aiogram.utils.mixins import T
from aiomysql import connection
from tgbot import config

from . import keyboards

from . import dbworker

from tgbot.database import connect, close_connection
from load_all import bot

async def start (message:types.Message):
    text = 'Привет, это бот для мобильной кофейни в Ростове-на-Дону. 👋\
        \n\nЧто бы ты хотел сделать?'
    con = await connect()
    user_id = message.from_user.id
    i = await dbworker.new_use(con, user_id)
    if i == 0:
        await message.reply(
            text=text,
            reply=False,
            reply_markup= await keyboards.start_keyboard_new(),
            disable_web_page_preview= True
    )
    else:
        await message.reply(
            text=text,
            reply=False,
            reply_markup= await keyboards.start_keyboard_old(),
            disable_web_page_preview= True
    )


def start_register(dp:Dispatcher):
    dp.register_message_handler(start, commands=['start'])