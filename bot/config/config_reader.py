import json
from typing import Any, Union

from pydantic import BaseSettings, validator


class TgBot(BaseSettings):
    """Telegram bot envs."""

    token: str
    admin_list: list[int]
    port: int
    use_redis: bool

    @validator("admin_list", pre=True, always=True)
    def admin_list_validator(cls, v: str) -> Union[list[int], Any]:
        return json.loads(v)


class Redis(BaseSettings):
    """Redis envs."""

    db: int
    host: str
    port: int


class Google(BaseSettings):
    """Google envs."""

    api: str
    email: str
    sheet_id: str


class Settings(BaseSettings):
    """To attributes sets name which correspond to prefix name (NAME__) from .env file
    and ignore prefix before add environmental variable to this config."""

    tg_bot: TgBot
    redis: Redis
    google: Google

    class Config:
        """Environmentals handler."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


def read_config(env_file=".env") -> Settings:
    """Create config."""
    config = Settings(_env_file=env_file)
    return config
