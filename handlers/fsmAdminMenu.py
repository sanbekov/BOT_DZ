from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMIN, bot
from database import bot_db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




class FSMAdmin(StatesGroup):
    photo_Dishes = State()
    name_Dishes = State()
    descriptions_Dishes = State()
    price_Dishes = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in ADMIN or message.chat.type == "private":
        await FSMAdmin.photo_Dishes.set()
        await message.answer(f"привет {message.from_user.full_name}: "
                             f"Скиньте фотку блюдо...")
    else:
        await message.reply("Пишите в личку!")

async def load_photo(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
         # data['id'] = message.from_user.id
         # data['username'] = f"@{message.from_user.username}"
         data['photo'] = message.photo[0].file_id
         await FSMAdmin.next()
         await message.answer("Названия блюдо?")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Описания блюдо?")

async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("Цена блюда?")

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
       data['price'] = float(message.text)
       await bot.send_photo(message.from_user.id, data['photo'],
                                 caption=f"Name: {data['name']}\n"
                                         f"description: {data['description']}\n"
                                         f"price: {data['price']}")
    await bot_db.sql_command_insert(state)
    await state.finish()
    await message.answer("Регитсрация завершена:")



async def cancel_registration(message: types.Message, state:FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Регистация отменена")

async def delete_data(message: types.Message):
    if message.from_user.id in ADMIN and message.chat.type == "private":
        global users
        users = await bot_db.sql_command_all()
        for user in users:
            await bot.send_photo(message.from_user.id, user[0],
                                 caption=f'Title: {user[1]}'
                                         f'Description: {user[2]}'
                                         f'Price: {user[3]}',
                                 reply_markup=InlineKeyboardMarkup().add(
                                     InlineKeyboardButton(
                                         f"delete: {user[1] }",
                                         callback_data=f"delete {user[1]}"
                                     )
                                 )
                                 )
    else:
        await message.reply("Ты не мой Босс!")


async def complete_delete(call: types.CallbackQuery):
    await bot_db.sql_command_delete(call.data.replace('delete ', ""))
    await call.answer(text=f"Блюдо {call.data.replace('delete ', '')} удалено из БД", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_fsmmenu(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*', commands='cansel')
    dp.register_message_handler(cancel_registration, Text(equals='cansel', ignore_case=True),state='*')

    dp.register_message_handler(fsm_start, commands=['register'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo_Dishes,
                               content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name_Dishes)
    dp.register_message_handler(load_description, state=FSMAdmin.descriptions_Dishes)
    dp.register_message_handler(load_price, state=FSMAdmin.price_Dishes)
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(
        complete_delete,
        lambda call: call.data and call.data.startswith("delete ")
    )

