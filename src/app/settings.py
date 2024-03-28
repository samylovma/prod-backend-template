from pydantic import AnyUrl, RedisDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: AnyUrl
    redis_url: RedisDsn
