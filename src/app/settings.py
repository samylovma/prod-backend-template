from pydantic import AnyUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: AnyUrl
