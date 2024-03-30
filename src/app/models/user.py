from typing import Annotated
from uuid import UUID, uuid4

from base import Base
from group import Group
from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO, SQLAlchemyDTOConfig
from sqlalchemy import LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user_to_group import association_table


class User(Base):
    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True, unique=True)
    login: Mapped[str]
    hashed_password: Mapped[bytes] = mapped_column(LargeBinary())
    children: Mapped[list[Group]] = relationship(secondary=association_table)


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
