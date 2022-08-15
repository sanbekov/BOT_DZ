import  random
from aiogram import types
from config import bot, ADMIN, Dispatcher



async def game(message: types.Message):
    if message.from_user.id in ADMIN and message.text.startswith('game'):
        games = ['🎯', '🎳', '🎲', '🎰', '🏀', '⚽️']
        r_games = random.choice(games)
        await bot.send_dice(message.chat.id, emoji=r_games)

def register_admin_handler(dp: Dispatcher):
    dp.register_message_handler(game)