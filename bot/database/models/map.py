from bot.database.models.quote import map_quote
from bot.database.models.user import map_user


# Collect all maps
def map_tables() -> None:
    map_quote()  # Quote
    map_user()  # User
