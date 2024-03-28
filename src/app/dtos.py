from typing import Annotated

from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import User

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
