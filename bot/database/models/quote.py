from dataclasses import dataclass, field

from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table, Text

from .base import mapper_registry


@dataclass
class Quote:
    id: int = field(init=False)
    quotation: str
    author: str
    by_user: int


quote_table = Table(
    "quote",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("quotation", Text),
    Column("author", String(50)),
    Column("by_user", String(12)),
)


def map_quote():
    mapper_registry.map_imperatively(Quote, quote_table)
