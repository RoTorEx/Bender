import asyncio

from aiogram import Bot, Dispatcher

from bot.config.config_reader import read_config
from bot.config.logger_builder import build_logger
from bot.database.connection import sa_sessionmaker
from bot.handlers import commands, messages
from bot.middlewares.db_session import DbSessionMiddleware


async def main():
    """Application entrypoint"""
    logger = build_logger(__name__)
    config = read_config()

    # Creating bot and its dispatcher
    bot = Bot(token=config.tg_bot.dev_token, parse_mode="HTML")
    dp = Dispatcher()

    # Creating DB connections pool
    session_pool = sa_sessionmaker(config.postgres, echo=False)

    # Register middlewares
    dp.message.middleware(DbSessionMiddleware(session_pool))
    dp.callback_query.middleware(DbSessionMiddleware(session_pool))

    dp.include_router(commands.router)
    dp.include_router(messages.router)

    try:
        logger.warning("Starting bot...")
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
