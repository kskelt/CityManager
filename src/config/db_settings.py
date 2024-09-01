"""Database connection settings.

This module describes the settings for connecting to the storage server and
settings for connecting to the database.

Attributes:
    db_settings (Settings): Instance of Settings class.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class DataBaseSettings(BaseSettings):
    """Data storage server and a database connection settings."""

    DATABASE_DIALECT: str
    DATABASE_DRIVER: str
    DATABASE_NAME: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    USER_NAME: str
    USER_PASSWORD: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


db_settings = DataBaseSettings()
