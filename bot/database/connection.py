from aiogram.dispatcher.fsm.storage.redis import DefaultKeyBuilder, RedisStorage

from bot.config.config_reader import Redis


def redis_conection(redis: Redis) -> RedisStorage:
    """Make connection to Redis."""
    storage = RedisStorage.from_url(
        url=f"redis://{redis.host}",
        connection_kwargs={
            "db": redis.db,
        },
        key_builder=DefaultKeyBuilder(with_destiny=True),
    )

    return storage
