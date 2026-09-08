from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Make app.* importable, and load the real DB URL + models from the app itself
# instead of duplicating config here.
from app.core.config import settings
from app.db.base import Base

# Import every model module so they register on Base.metadata before autogenerate runs.
from app.models import (  # noqa: F401
    user, venue, spatial_znt, revenue_prediction, tax_payment, anomaly_result, sustainability_result,
)

config = context.config
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
