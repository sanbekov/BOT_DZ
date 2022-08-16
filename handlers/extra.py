from aiogram import types
from config import bot, Dispatcher, ADMIN
import random


#dp.message_handler()
async def echo(message: types.Message):
    if message.from_user.id in ADMIN and message.text.startswith('game'):
        games = ['g', '🎳', '🎲', '🎰', '🏀', '⚽️']
        r_games = random.choice(games)
        await bot.send_dice(message.chat.id, emoji=r_games)
    elif  message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) * int(message.text))
    else:
        await bot.send_message(message.from_user.id, message.text)



#@dp.message_handler()
async def ban(message: types.Message):
    bad_words = ['дамон', 'bitch', 'lox', 'жинди', 'тупой']
    username = f"@{message.from_user.username}" if message.from_user.username is not None else ""
    for word in bad_words:
        if word in message.text.lower():
            await bot.send_message(
                message.chat.id,
                f"Не матерись {message.from_user.full_name}, "
                f"сам ты {word} {username}"
            )
            await bot.delete_message(message.chat.id, message.message_id)





def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
    dp.register_message_handler(ban)

