import asyncio
from typing import Union

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from aiogram.dispatcher.fsm.storage.redis import RedisStorage

from bot.config import build_logger, read_config
from bot.database import redis_conection
from bot.handlers import awards_router, commands_router


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

    # Register routers
    dp.include_router(awards_router)
    dp.include_router(commands_router)

    try:
        await dp.start_polling(bot)

    finally:
        await dp.fsm.storage.close()
        await bot.session.close()


if __name__ == "__main__":
    logger = build_logger(__name__)

    try:
        logger.info("Starting bot...")
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        logger.warning("All pools and session closed. Bot stopped successfully!")
