from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base, CustomBaseModel, mapper_registry


class Quote(Base):
    """Quote table."""

    __tablename__ = "quote"

    id = Column(Integer, primary_key=True)
    quotation = Column(Text)
    author = Column(String)
    user = relationship("Customer")
    from_user = Column(Integer, ForeignKey("customer.id"))
    time = Column(String)
    is_confirmed = Column(Boolean)
    is_active = Column(Boolean)


class QuoteSchema(CustomBaseModel):
    """Pydantic validation schema to Quote table."""

    id: int
    quotation: str
    author: str
    from_user: int
    time: str
    is_confirmed: bool
    is_active: bool


def map_quote() -> None:
    """Register models."""
    mapper_registry.map_imperatively(Quote)
