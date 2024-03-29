from typing import Any

from litestar import Litestar
from litestar.connection import ASGIConnection
from litestar.contrib.sqlalchemy.plugins import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)
from litestar.middleware.session.server_side import (
    ServerSideSessionBackend,
    ServerSideSessionConfig,
)
from litestar.security.session_auth import SessionAuth
from litestar.stores.redis import RedisStore
from redis.asyncio import Redis

from app import controllers
from app.dependencies import provide_user_service
from app.models import User
from app.settings import Settings


async def retrieve_user_handler(
    session: dict[str, Any], connection: ASGIConnection[Any, Any, Any, Any]
) -> User | None:
    db_session = await connection.app.dependencies["db_session"](
        state=connection.app.state, scope=connection.scope
    )
    user_service = await provide_user_service(db_session)
    return await user_service.get_one_or_none(id=session["user_id"])


def create_app() -> Litestar:
    settings = Settings()
    auth = SessionAuth[User, ServerSideSessionBackend](
        retrieve_user_handler=retrieve_user_handler,
        session_backend_config=ServerSideSessionConfig(),
        exclude=["/schema", "/users", "/access/login", "/access/signup"],
    )
    return Litestar(
        route_handlers=[
            controllers.UserController,
            controllers.AccessController,
            controllers.MeController,
        ],
        on_app_init=[auth.on_app_init],
        plugins=[
            SQLAlchemyPlugin(
                config=SQLAlchemyAsyncConfig(
                    connection_string=str(settings.database_url),
                    session_config=AsyncSessionConfig(expire_on_commit=False),
                )
            )
        ],
        stores={"sessions": RedisStore(redis=Redis.from_url(str(settings.redis_url)))},
    )
