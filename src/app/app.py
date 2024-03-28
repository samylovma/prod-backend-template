import os

from litestar import Litestar
from litestar.contrib.sqlalchemy.plugins import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)

from app import controllers


def create_app() -> Litestar:
    return Litestar(
        route_handlers=[controllers.UserController],
        plugins=[
            SQLAlchemyPlugin(
                config=SQLAlchemyAsyncConfig(
                    connection_string=os.getenv("DATABASE_URL"),
                    session_config=AsyncSessionConfig(expire_on_commit=False),
                )
            )
        ],
    )
