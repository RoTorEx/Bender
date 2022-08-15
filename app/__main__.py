import asyncio
import os

from aiogram import Bot, Dispatcher, types
from utils.bot_logger import create_logger


async def main():
    logger.warning("Starting bot...")

    bot_token = os.environ.get('TG_BOT__DEV_TOKEN')
    bot = Bot(token=bot_token)
    dp = Dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logger = create_logger(__name__)
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        logger.warning("Bot stopped!")
