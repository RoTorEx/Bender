from aiogram.dispatcher.fsm.storage.redis import DefaultKeyBuilder, RedisStorage
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from bot.config.config_reader import Postgres, Redis


def database_path(db: Postgres, async_fallback: bool = False) -> str:
    """Make path to Postgres database."""
    path = f"postgresql+asyncpg://{db.user}:{db.password}@{db.host}:{db.port}/{db.name}"

    if async_fallback:
        path += "?async_fallback=True"

    return path


def sa_sessionmaker(db: Postgres, echo: bool = False) -> sessionmaker:
    """Make async sessionmaker."""
    engine = create_async_engine(database_path(db), echo=echo)

    return sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession,
        future=True,
        autoflush=False,
    )


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
