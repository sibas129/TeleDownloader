import asyncio
import logging

from aiogram import Bot, types, F
from aiogram import Dispatcher

from handlers import user_commands, echo, uploader

import config


dp = Dispatcher()
bot = Bot(token=config.TOKEN)


async def main():
    logging.basicConfig(level=logging.INFO)

    dp.include_routers(
        user_commands.router,
        uploader.router,
        echo.router
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
