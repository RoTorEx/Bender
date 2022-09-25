import json

from pydantic import BaseSettings, validator


class Redis(BaseSettings):
    """Redis envs."""

    db: int
    host: str
    port: int


class Postgres(BaseSettings):
    """Postgres envs."""

    name: str
    user: str
    password: str
    host: str
    port: int


class TgBot(BaseSettings):
    """Telegram bot envs."""

    prod_token: str
    dev_token: str
    admin_list: list[int]
    port: int
    use_redis: bool

    @validator("admin_list", pre=True, always=True)
    def admin_list_validator(cls, v) -> list[int]:
        return json.loads(v)


class Settings(BaseSettings):
    """To attributes sets name which correspond to prefix name (NAME__) from .env file
    and ignore prefix before add environmental variable to this config."""

    tg_bot: TgBot
    redis: Redis
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
