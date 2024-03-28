from typing import Any, Self

from litestar import Controller, Request
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import post
from litestar.status_codes import HTTP_200_OK

from app.dependencies import provide_user_service
from app.models import User, UserReadDTO
from app.schemas import UserCreate, UserLogin
from app.services import UserService


class AccessController(Controller):
    path = "/access"
    dependencies = {"user_service": Provide(provide_user_service)}  # noqa: RUF012

    @post("/login", status_code=HTTP_200_OK)
    async def login(
        self: Self,
        data: UserLogin,
        request: Request[Any, Any, Any],
        user_service: UserService,
    ) -> None:
        user = await user_service.get(data.id)
        request.set_session({"user_id": user.id})

    @post("/logout", status_codes=HTTP_200_OK)
    async def logout(self: Self, request: Request[Any, Any, Any]) -> None:
        request.cookies.pop("session", None)
        request.clear_session()

    @post("/signup", return_dto=UserReadDTO)
    async def signup(
        self: Self,
        data: UserCreate,
        request: Request[Any, Any, Any],
        user_service: UserService,
    ) -> User:
        user = await user_service.create(data.model_dump())
        request.set_session({"user_id": user.id})
        return user
