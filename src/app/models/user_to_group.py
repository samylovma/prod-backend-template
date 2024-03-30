from msilib import Table

from base import Base
from sqlalchemy import Column, ForeignKey

association_table = Table(
    "user_to_group",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("group_id", ForeignKey("group.id")),
)
