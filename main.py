from aiogram import executor
from config import dp
from handlers import (
    start,
)
from database import bot_dp
async def on_startup(_):
    dp = bot_dp.Database()
    dp.sql_create_tables()

start.register_start_handler(dp=dp)


if __name__ == "__main__":
    executor.start_polling(
        dp,
        on_startup=on_startup
    )