from litestar import Litestar
from litestar.contrib.sqlalchemy.plugins import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)

from app import controllers
from app.settings import Settings


def create_app() -> Litestar:
    settings = Settings()
    return Litestar(
        route_handlers=[controllers.UserController],
        plugins=[
            SQLAlchemyPlugin(
                config=SQLAlchemyAsyncConfig(
                    connection_string=str(settings.database_url),
                    session_config=AsyncSessionConfig(expire_on_commit=False),
                )
            )
        ],
    )
