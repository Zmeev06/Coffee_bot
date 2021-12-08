from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, callback_query
from aiogram.types.inline_keyboard import InlineKeyboardMarkup
from aiogram.utils import callback_data
from aiogram.utils.callback_data import CallbackData


async def start_keyboard_new():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            text='Пройти стажировку',
            callback_data = 'start_new_user'
        ))
    return markup

async def start_keyboard_old():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton (
            text = 'Войти как бариста',
            callback_data='old_user'
        ),
        InlineKeyboardButton (
            text = 'Войти как работодатель',
            callback_data='admin_start'
        ))
    return markup