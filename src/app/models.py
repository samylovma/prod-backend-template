from typing import Annotated
from uuid import UUID, uuid4

from advanced_alchemy.base import CommonTableAttributes, orm_registry
from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO, SQLAlchemyDTOConfig
from sqlalchemy import LargeBinary
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(CommonTableAttributes, DeclarativeBase):
    registry = orm_registry


class User(Base):
    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    hashed_password: Mapped[bytes] = mapped_column(LargeBinary())


UserReadDTO = SQLAlchemyDTO[
    Annotated[
        User,
        SQLAlchemyDTOConfig(
            exclude={
                "hashed_password",
            },
            rename_strategy="camel",
        ),
    ]
]
