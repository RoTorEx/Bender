from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    tg_bot__dev_token: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
