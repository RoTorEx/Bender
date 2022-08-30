from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table, Text

from .base import mapper_registry, meta


quote_table = Table(
    "quote",
    mapper_registry.metadata,
    # MetaData(),
    Column("id", Integer(), primary_key=True),
    Column("quotaion", Text(), nullable=False),
)


class Quote:
    pass


def map_quote():
    mapper_registry.map_imperatively(Quote, quote_table)
