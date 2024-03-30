from advanced_alchemy.base import CommonTableAttributes, orm_registry
from sqlalchemy.orm import DeclarativeBase


class Base(CommonTableAttributes, DeclarativeBase):
    registry = orm_registry
