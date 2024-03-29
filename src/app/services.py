from typing import Any, Self
from uuid import UUID

from advanced_alchemy import SQLAlchemyAsyncRepositoryService
from litestar.exceptions import PermissionDeniedException

from app.crypt import check_password, hash_password
from app.models import User
from app.repositories import UserRepository


class UserService(SQLAlchemyAsyncRepositoryService[User]):
    repository_type = UserRepository

    async def to_model(
        self: Self, data: User | dict[str, Any], operation: str | None = None
    ) -> User:
        if isinstance(data, dict) and "password" in data:
            password: str = data.pop("password")
            data["hashed_password"] = hash_password(password)
        return await super().to_model(data=data, operation=operation)

    async def authenticate(self: Self, id_: UUID, password: str) -> User:
        user = await self.get_one_or_none(id=id_)
        if user is None:
            msg = "User not found"
            raise PermissionDeniedException(msg)
        if not check_password(password, user.hashed_password):
            msg = "Invalid password"
            raise PermissionDeniedException(msg)
        return user
