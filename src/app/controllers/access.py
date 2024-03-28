from typing import Any, Self

from litestar import Controller, Request
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import post
from litestar.status_codes import HTTP_200_OK

from app.dependencies import provide_user_service
from app.models import UserReadDTO
from app.schemas import UserLogin
from app.services import UserService


class AccessController(Controller):
    path = "/access"
    dependencies = {"user_service": Provide(provide_user_service)}  # noqa: RUF012

    @post("/login", return_dto=UserReadDTO, status_code=HTTP_200_OK)
    async def login(
        self: Self,
        data: UserLogin,
        request: Request[Any, Any, Any],
        user_service: UserService,
    ) -> None:
        user = await user_service.get(data.id)
        request.set_session({"user_id": user.id})

    @post("/logout")
    async def logout(self: Self, request: Request[Any, Any, Any]) -> None:
        request.cookies.pop("session", None)
        request.clear_session()
