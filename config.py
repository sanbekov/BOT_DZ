from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = [5372743154]
URL = " https://python21bot.herokuapp.com/"