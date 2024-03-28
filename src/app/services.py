from typing import Any, Self

from advanced_alchemy import SQLAlchemyAsyncRepositoryService

from app.crypt import hash_password
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
