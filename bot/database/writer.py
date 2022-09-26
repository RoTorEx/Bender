import datetime
from contextlib import suppress

from aiogram.types.user import User
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from bot.config.constants import TgBot
from bot.config.logger_builder import build_logger
from bot.database.models.customer import Customer, CustomerSchema
from bot.database.models.quote import Quote
from bot.utils.user_to_string import make_customer_string


logger = build_logger(__name__)


async def write_new_customer(message_user: User, session: AsyncSession) -> None:
    """Write new customer to database."""
    customer = Customer()
    customer.customer_id = message_user.id
    customer.customer_nickname = message_user.username if message_user.username else None
    customer.customer_full_name = make_customer_string(
        {"first_name": message_user.first_name, "last_name": message_user.last_name}
    )
    customer.is_admin = True if message_user.id in TgBot.admin_list else False
    customer.is_active = True

    session.add(customer)

    with suppress(IntegrityError):
        await session.commit()
        TgBot.customer_list.append(message_user.id)
        logger.info(
            f"New user! {customer.customer_full_name} ({customer.customer_nickname}) with {customer.customer_id} id."
        )


async def write_new_quote(data: dict, session: AsyncSession) -> None:
    """Write quote to database."""
    statement = select(Customer).where(Customer.customer_id == data["quote_author"]["id"])
    result = await session.execute(statement)

    table_id = CustomerSchema.from_orm(result.scalar()).id

    quote = Quote()
    quote.quotation = data["quote"]
    quote.author = data["author"]
    quote.from_user = table_id
    quote.time = datetime.datetime.utcnow().strftime("%y-%m-%d %H:%M")
    # quote.is_confirmed = True if data["quote_sender_id"] in TgBot.admin_list else False
    quote.is_confirmed = True  # Temp
    quote.is_active = True

    session.add(quote)

    with suppress(IntegrityError):
        await session.commit()
        logger.info(f"New quote was added! '{quote.quotation}' © {quote.author}.")
