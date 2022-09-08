from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base, mapper_registry


class Quote(Base):
    """Quote table."""

    __tablename__ = "quote"

    id = Column(Integer, primary_key=True)
    quotation = Column(Text)
    author = Column(String)
    user = relationship("TgUser")
    from_user_id = Column(Integer, ForeignKey("user.id"))


def map_quote() -> None:
    """Register models."""
    mapper_registry.map_imperatively(Quote)
