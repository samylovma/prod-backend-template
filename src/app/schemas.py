import pydantic
from pydantic.alias_generators import to_camel


class UserCreate(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(alias_generator=to_camel)

    first_name: str
    last_name: str
    password: str
