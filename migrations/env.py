from src.config.db_settings import db_settings
from sqlalchemy import create_engine, pool
from logging.config import fileConfig
from alembic import context
from src.db.tables import City  # Import your Base here

# Interpret the config file for Python logging.
fileConfig(context.config.config_file_name)
database_url = (
    f"{db_settings.DATABASE_DIALECT}+"
    f"{db_settings.DATABASE_DRIVER}"
    f"://{db_settings.USER_NAME}:"
    f"{db_settings.USER_PASSWORD}"
    f"@{db_settings.DATABASE_HOST}:"
    f"{db_settings.DATABASE_PORT}"
    f"/{db_settings.DATABASE_NAME}"
)

target_metadata = City.metadata

def run_migrations_offline() -> None:
    context.configure(url=database_url, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = create_engine(database_url)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
