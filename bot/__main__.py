import asyncio
from typing import Union

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from aiogram.dispatcher.fsm.storage.redis import RedisStorage

from bot.config.config_reader import read_config
from bot.config.constants import TgBot
from bot.config.logger_builder import build_logger
from bot.database.connection import redis_conection, sa_sessionmaker
from bot.database.reader import get_all_customers
from bot.handlers import commands, messages_quote_dialog
from bot.middlewares.db_session import DbSessionMiddleware


async def main() -> None:
    """Application entrypoint"""
    config = read_config()

    # Choosing Memory Storage
    storage: Union[RedisStorage, MemoryStorage]
    if config.tg_bot.use_redis:
        storage = redis_conection(config.redis)

    else:
        storage = MemoryStorage()

    # Creating bot and its dispatcher
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher(storage=storage)

    # Creating DB connections pool
    session_pool = sa_sessionmaker(config.postgres, echo=False)

    # Register middlewares
    dp.message.middleware(DbSessionMiddleware(session_pool))
    dp.callback_query.middleware(DbSessionMiddleware(session_pool))

    # Register routers
    dp.include_router(commands.router)
    dp.include_router(messages_quote_dialog.router)

    # Create contants dataclass
    TgBot.bot = bot
    TgBot.admin_list = config.tg_bot.admin_list
    TgBot.customer_list = await get_all_customers(session_pool)

    try:
        await dp.start_polling(bot)

    finally:
        await dp.fsm.storage.close()
        await bot.session.close()


if __name__ == "__main__":
    logger = build_logger(__name__)

    try:
        logger.warning("Starting bot...")
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        logger.warning("All pools and session closed. Bot stopped successfully!")
