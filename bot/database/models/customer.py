from sqlalchemy import BigInteger, Boolean, Column, Integer, String

from bot.database.models.base import Base, CustomBaseModel, mapper_registry


class Customer(Base):
    """Customer table."""

    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    customer_id = Column(BigInteger, unique=True)
    customer_nickname = Column(String)
    customer_full_name = Column(String)
    is_admin = Column(Boolean)
    is_active = Column(Boolean)


class CustomerSchema(CustomBaseModel):
    """Pydantic validation schema to Customer table."""

    id: int
    customer_id: int
    customer_nickname: str
    customer_full_name: str
    is_admin: bool
    is_active: bool


def map_customer() -> None:
    """Register models."""
    mapper_registry.map_imperatively(Customer)
