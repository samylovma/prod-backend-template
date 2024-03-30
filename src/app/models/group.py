from typing import Annotated
from uuid import UUID, uuid4

from base import Base
from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO
from sqlalchemy.orm import Mapped, mapped_column


class Group(Base):
    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True, unique=True)


GroupReadDTO = SQLAlchemyDTO[
    Annotated[
        Group,
    ]
]
