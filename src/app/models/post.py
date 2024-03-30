from typing import Annotated
from uuid import UUID, uuid4

from base import Base
from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Post(Base):
    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True, unique=True)
    name: Mapped[str]
    group_id: Mapped[UUID]
    text: Mapped[str]
    message_id: Mapped[int]
    publish_at: Mapped[DateTime]
    published_at: Mapped[DateTime]


PostReadDTO = SQLAlchemyDTO[
    Annotated[
        Post,
    ]
]
