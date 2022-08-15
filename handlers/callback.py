from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot

#@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def hana_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)
    question = "Кто придумал Таеквондо"
    answers = [
        "Генерал Чой Хон Хи",
        "Генерал Гевс",
        "Генерал Лебедь",
        "Генерал Айтегин"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=10,
        explanation="Анти Скачок",
        reply_markup=markup
    )

#@dp.callback_query_handler(lambda call: call.data == 'button_call_2')
async def hana_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Что означает черный пояс в Таеквондо"
    answers = [
        "Цвет мудрости. Черный цвет объединяет в себе все цвета спектра",
        "Цвет снега, цвет рождения жизни, цвет начала нового года",
        "Цвет расцветающей природы, цвет лета",
        "Цвет спелости плодов и зрелости знания, цвет осени"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=10,
        explanation="Ты шутишь?"
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(hana_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(hana_3, lambda call: call.data == 'button_call_2')