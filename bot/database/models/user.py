from sqlalchemy import Column, Integer, String

from .base import Base, mapper_registry


class TgUser(Base):
    """User table."""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, )
    user_nickname = Column(String)
    user_full_name = Column(String)


def map_user() -> None:
    """Register models."""
    mapper_registry.map_imperatively(TgUser)
