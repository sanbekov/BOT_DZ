from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, admin
import logging

client.register_handlers_client(dp)
admin.register_admin_handler(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


