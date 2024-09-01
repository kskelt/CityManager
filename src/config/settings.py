"""This module describes the settings for connecting to the storage server.

Attributes:
    settings (Settings): Instance of Settings class.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SERVER_HOST: str
    SERVER_PORT: int

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
