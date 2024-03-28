from sqlalchemy.ext.asyncio import AsyncSession

from app.services import UserService


async def provide_user_service(db_session: AsyncSession) -> UserService:
    return UserService(session=db_session, auto_commit=True)
