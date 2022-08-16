import random
from aiogram import types
from config import bot, ADMIN, Dispatcher


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:
            await message.reply('Ты не Деймон отвали!!')
        elif not message.reply_to_message:
            await message.reply("Команда должно быть ответом на сообщения")
        else:
            await bot.kick_chat_member(
                message.chat.id,
                user_id=message.reply_to_message.from_user
            )
            await message.answer(f"{message.from_user.first_name}cабоним" 
                               f"Абанил тебя деймон{message.reply_to_message.from_user.full_name}")
    else:
            await message.reply("Пиши в группу!")


def register_handler_admin(dp:Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix="!/")




