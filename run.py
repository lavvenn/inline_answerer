import asyncio

from aiogram import Bot, Dispatcher

from app.handlers import router
from app.inline import irouter

from config import TOKEN

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_router(router)
    dp.include_router(irouter)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())