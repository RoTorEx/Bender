from bot.database.models.customer import map_customer
from bot.database.models.quote import map_quote


# Collect all maps
def map_tables() -> None:
    map_customer()  # Customer
    map_quote()  # Quote
