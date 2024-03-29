from typing import Any, Self

from litestar import Controller, Request, get
from litestar.di import Provide

from app.dependencies import provide_user_service
from app.models import User, UserReadDTO


class MeController(Controller):
    path = "/me"
    dependencies = {"user_service": Provide(provide_user_service)}  # noqa: RUF012

    @get(return_dto=UserReadDTO)
    async def profile(self: Self, request: Request[User, Any, Any]) -> User:
        return request.user
