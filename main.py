from aiogram.utils import executor
from config import dp, URL, bot
from handlers import client, callback, extra, admin, fsmAdminMenu, notificatione, inline
from database import bot_db
import logging
import asyncio
import config
async def on_startup(_):
    await bot.send_webhook(URL)
    asyncio.create_task(notificatione.scheduler())
    bot_db.sql_create()

async def on_shutdown(dp):
    await bot.delete_webhook()


client.register_handlers_client(dp)
admin.register_handler_admin(dp)
callback.register_handlers_callback(dp)
fsmAdminMenu.register_handlers_fsmmenu(dp)
notificatione.register_handler_notification(dp)
inline.register_handler_inline(dp)

extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    #executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    executor.set_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=config("PORT", cast=int)


    )
