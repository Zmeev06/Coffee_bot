import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ParseMode, chat, message, user
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
    shifts = State()

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
    await state.update_data(name=name)
    await message.answer('Отлично, теперь укажи свою фамилию')

    await New_user.second_name.set()


async def set_age (message:types.Message, state:FSMContext):
    second_name = message.text

    await state.update_data(second_name=second_name)

    await message.answer('Сколько вам лет?')
    await New_user.age.set()


async def experience (message: types.Message, state:FSMContext):
    age = message.text
    await state.update_data(age=age)
    await message.reply(
        text='У вас есть опыт работы?',
        reply_markup=await keyboards.exp(),
        reply=False,
        disable_web_page_preview=True
    )
    user_id = message.from_user.id
    user_data =await state.get_data()
    name = user_data['name']
    second_name = user_data['second_name']
    age = user_data['age']
    exp = 0
    con = await connect()
    await dbworker.new_user(con, user_id, name, second_name, age)
    await close_connection(con)
    await state.finish()

async def no_exp(call:types.CallbackQuery ):
    user_id = call.from_user.id
    user_id = int(user_id)
    con = await connect()
    await dbworker.exp(con, exp=0, user_id=user_id) 
    await close_connection(con)
    await call.answer()
    await call.message.reply(text='Укажите в какие дни вы можете выходить на работу\
        \n\n<b>Примечание</b>\
        \nВремя дневной смены: 7:00-15:00\
        \nВремя вечерней смены: 17:00-2:00',
        reply= False,
        disable_web_page_preview= True,
        reply_markup= await keyboards.shifts())

async def min_exp(call:types.CallbackQuery):
    user_id = call.from_user.id
    user_id = int(user_id)
    con = await connect()
    await dbworker.exp(con, exp=1, user_id=user_id) 
    await close_connection(con)
    await call.answer()
    await call.message.reply(text='Укажите в какие дни вы можете выходить на работу\
        \n\n<b>Примечание</b>\
        \nВремя дневной смены: 7:00-15:00\
        \nВремя вечерней смены: 17:00-2:00',
        reply= False,
        disable_web_page_preview= True,
        reply_markup= await keyboards.shifts())

async def max_exp(call:types.CallbackQuery):
    user_id = call.from_user.id
    user_id = int(user_id)
    con = await connect()
    await dbworker.exp(con, exp=2, user_id=user_id) 
    await close_connection(con)
    await call.answer()
    await call.message.reply(text='Укажите в какие дни вы можете выходить на работу\
        \n\n<b>Примечание</b>\
        \nВремя дневной смены: 7:00-15:00\
        \nВремя вечерней смены: 17:00-2:00',
        reply= False,
        disable_web_page_preview= True,
        reply_markup= await keyboards.shifts())
    
async def all_shifts(call:types.CallbackQuery):
    user_id = call.from_user.id
    user_id = int(user_id)
    con = await connect()
    await dbworker.shifts(con, shifts='all', user_id=user_id) 
    await close_connection(con)
    await call.answer()


async def evn_shifts(call:types.CallbackQuery):
    user_id = call.from_user.id
    user_id = int(user_id)
    con = await connect()
    await dbworker.shifts(con, shifts='evn', user_id=user_id) 
    await close_connection(con)
    await call.answer()


async def day_shifts(call:types.CallbackQuery):
    user_id = call.from_user.id
    user_id = int(user_id)
    con = await connect()
    await dbworker.shifts(con, shifts='day', user_id=user_id) 
    await close_connection(con)
    await call.answer()


async def evn_day(call:types.CallbackQuery):
    user_id = call.from_user.id
    user_id = int(user_id)
    con = await connect()
    await dbworker.shifts(con, shifts='evn_day', user_id=user_id) 
    await close_connection(con)
    await call.answer()
    await call.message.reply(
        text='Отлично! Теперь укажите от кого вы попали в данного бота и можем приступать к стажировке',
        reply=False,
        disable_web_page_preview=True,
        reply_markup= await keyboards.employer()
    )



def new_user_register(dp:Dispatcher):
    dp.register_callback_query_handler(new_user_name, text='start_new_user')
    dp.register_message_handler(new_user_second_name, state=New_user.name)
    dp.register_message_handler(set_age, state=New_user.second_name)
    dp.register_message_handler(experience, state=New_user.age)
    dp.register_callback_query_handler(no_exp, text='no_exp')
    dp.register_callback_query_handler(min_exp, text='1_year_exp')
    dp.register_callback_query_handler(max_exp, text='more_1_year_exp')
    dp.register_callback_query_handler(all_shifts, text='all_shifts')
    dp.register_callback_query_handler(evn_shifts, text='all_evn')
    dp.register_callback_query_handler(day_shifts, text='all_day')
    dp.register_callback_query_handler(evn_day, text='evn_day')

