import asyncio

from aiogram import Bot, Dispatcher

from bot.config.config_reader import read_config
from bot.config.logger_builder import build_logger
from bot.database.connection import sa_sessionmarker
from bot.handlers import commands


async def main():
    """Application entrypoint"""
    logger.warning("Starting bot...")

    bot = Bot(token=config.tg_bot.dev_token)
    dp = Dispatcher()
    dp.include_router(commands.router)

    session = sa_sessionmarker(config.postgres)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        config = read_config()
        logger = build_logger(__name__)

        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        logger.warning("Bot stopped!")
