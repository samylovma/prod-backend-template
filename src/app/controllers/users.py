from typing import Self
from uuid import UUID

from litestar import Controller, get, post
from litestar.di import Provide

from app.dependencies import provide_user_service
from app.models import User, UserReadDTO
from app.schemas import UserCreate
from app.services import UserService


class UserController(Controller):
    path = "/users"
    dependencies = {"user_service": Provide(provide_user_service)}  # noqa: RUF012
    return_dto = UserReadDTO

    @post()
    async def create_user(
        self: Self, data: UserCreate, user_service: UserService
    ) -> User:
        return await user_service.create(data.model_dump())

    @get("/{user_id:uuid}")
    async def get_user(self: Self, user_id: UUID, user_service: UserService) -> User:
        return await user_service.get(user_id)
