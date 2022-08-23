from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from bot.config.config_reader import Postgres


def database_path(db: Postgres):
    """Make path to Postgres database."""
    path = f"postgresql+asyncpg://{db.name}:{db.password}@{db.host}:{db.port}/{db.name}"
    return path


def sa_sessionmarker(db: Postgres):
    """Make sessionmaker."""
    engine = create_async_engine(database_path(db), echo=False)
    return engine
