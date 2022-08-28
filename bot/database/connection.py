from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from bot.config.config_reader import Postgres


def database_path(db: Postgres, async_fallback: bool = False) -> str:
    """Make path to Postgres database."""
    path = f"postgresql+asyncpg://{db.name}:{db.password}@{db.host}:{db.port}/{db.name}"

    if async_fallback:
        path += "?async_fallback=True"

    return path


def sa_sessionmarker(db: Postgres) -> sessionmaker:
    """Make sessionmaker."""
    engine = create_async_engine(database_path(db), echo=True)

    return sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession,
        future=True,
        autoflush=False,
    )
