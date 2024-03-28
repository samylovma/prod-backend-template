from advanced_alchemy import SQLAlchemyAsyncRepository

from app.models import User


class UserRepository(SQLAlchemyAsyncRepository[User]):
    model_type = User
