import random

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from bot.config.logger_builder import build_logger
from bot.database.models.customer import Customer
from bot.database.models.quote import Quote


logger = build_logger(__name__)


async def get_all_customers(session_pool: sessionmaker) -> list:
    """Get list of all registered customers."""
    async with session_pool() as session:
        statement = select(Customer.customer_id).where(Customer.is_active == bool(1))
        result = await session.execute(statement)

    return list(filter(lambda x: isinstance(x, int), result.scalars().all()))


async def read_random_quote(session: AsyncSession) -> str:
    """Read random quote from database."""
    statement = select(Quote).where(Quote.is_active == bool(1)).where(Quote.is_confirmed == bool(1))
    result = await session.execute(statement)
    quote_list = result.scalars().all()

    if quote_list:
        quote = random.choice(quote_list)
        return f"```\n{quote.quotation}\n```\n© {quote.author}"

    else:
        return "Quote collection is empty :'("
