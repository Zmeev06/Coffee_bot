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
    return markup


async def shifts():
    markup=InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            text='Будни и выходные дневная и вечерняя смены',
            callback_data='all_shifts'
        ),
        InlineKeyboardButton(
            text='Будни и выходные только вечерняя смена',
            callback_data='all_evn'
        ),
        InlineKeyboardButton(
            text='Будни и выходные только дневная смена',
            callback_data='all_day'
        ),
        InlineKeyboardButton(
            text='В будни только вечерняя смена, в выходные могу и дневную',
            callback_data='evn_day'
        )
    )
    return markup


async def employer():
    markup=InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            text='Роман К.',
            callback_data='roman'
        ),
        InlineKeyboardButton(
            text='Дмитрий Деренский',
            callback_data='dima'
        ),
        InlineKeyboardButton(
            text='Сергей',
            callback_data='sergey'
        )
    )
    return markup