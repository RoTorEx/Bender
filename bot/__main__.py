import asyncio

from aiogram import Bot, Dispatcher, types

from bot.config.config_reader import config
from bot.config.logger_config import create_logger


async def main():
    logger.warning("Starting bot...")

    bot = Bot(token=config.tg_bot__dev_token.get_secret_value())
    dp = Dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logger = create_logger(__name__)
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        logger.warning("Bot stopped!")
