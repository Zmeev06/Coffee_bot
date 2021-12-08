import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from tgbot.config import load_config

logger = logging.getLogger(__name__)


config = load_config("bot.ini")
storage = MemoryStorage()
bot = Bot(token=config.tg_bot.token, parse_mode=ParseMode.HTML)
DP = Dispatcher(bot, storage=storage)

