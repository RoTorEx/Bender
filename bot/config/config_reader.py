import json

from pydantic import BaseSettings, validator


class TgBot(BaseSettings):
    """Telegram bot envs."""
    prod_token: str
    dev_token: str
    admin_ids: list[int]
    port: int

    @validator("admin_ids", pre=True, always=True)
    def admin_ids_list(cls, v) -> list[int]:
        return json.loads(v)


class Postgres(BaseSettings):
    """Postgres envs."""
    name: str
    user: str
    password: str
    host: str
    port: int


class Settings(BaseSettings):
    """To atributes set name wich correspond to preffix name (NAME__) in .env file."""
    tg_bot: TgBot
    postgres: Postgres

    class Config:
        """Environmentals handler."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


def read_config() -> Settings:
    """Create config."""
    config = Settings()
    return config
