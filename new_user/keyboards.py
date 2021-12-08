from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, callback_query
from aiogram.types.inline_keyboard import InlineKeyboardMarkup
from aiogram.utils import callback_data
from aiogram.utils.callback_data import CallbackData

async def exp():
    markup=InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            text='Нет опыта работы бариста',
            callback_data='no_exp'
        ),
        InlineKeyboardButton(
            text='Опыт работы менее года',
            callback_data='1_year_exp'
        ),
        InlineKeyboardButton(
            text='Опыт работы более года',
            callback_data='more_1_year_exp'
        )
    )