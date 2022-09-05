import random
from pprint import pprint

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import hbold
from config import bot, Dispatcher
from aiogram import types
from database.bot_db import sql_command_random
from perser.fighter import parser


#@dp.message_handler(commands=['hana'])
async def hana_1(message:types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Сколько принципов в Таеквондо"
    answers = [
        "10",
        "8",
        "2",
        "5"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        open_period=10,
        explanation="Сачок",
        reply_markup=markup
    )

#@dp.message_handler(commands=['mem'])
async def start_handler(message: types.Message):
    photos = ['media/mem3.jpg', 'media/baa.jpg', 'media/mem.jpg']
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.chat.id, photo=photo)

async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

async def show_random_user(message:types.Message):
    await sql_command_random(message)

async def parser_fighter(message: types.Message):
    data = parser()
    for item in data:
        title = hbold(item['title'])
        await bot.send_message(
            message.from_user.id,
            f"{item['link']}\n\n"
            f"{item['title']}\n"
            f"#{item['year']}\n"
            f"#{item['city']}\n"
            f"#{item['genre']}\n"
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hana_1, commands=['hana'])
    dp.register_message_handler(start_handler, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(show_random_user,  commands=['get'])
    dp.register_message_handler(parser_fighter, commands=['fighter'])
