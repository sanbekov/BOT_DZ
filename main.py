from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, admin, fsmAdminMenu
from database import bot_db
import logging


async def on_startup(_):
    bot_db.sql_create()


client.register_handlers_client(dp)
admin.register_handler_admin(dp)
callback.register_handlers_callback(dp)
fsmAdminMenu.register_handlers_fsmmenu(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
