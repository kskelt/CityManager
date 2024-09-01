from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.db_settings import db_settings

database_url = (
    f"{db_settings.DATABASE_DIALECT}+"
    f"{db_settings.DATABASE_DRIVER}"
    f"://{db_settings.USER_NAME}:"
    f"{db_settings.USER_PASSWORD}"
    f"@{db_settings.DATABASE_HOST}:"
    f"{db_settings.DATABASE_PORT}"
    f"/{db_settings.DATABASE_NAME}"
)

engine = create_engine(database_url)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session() -> Any | None:
    session = Session()
    try:
        yield session
    finally:
        session.close()
