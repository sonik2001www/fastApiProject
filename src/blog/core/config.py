import os
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    DATABASE_URL: str = Field("postgresql://user:password@db:5432/blog", env="DATABASE_URL")
    PROJECT_NAME: str = "Blog API"
    SECRET_KEY: str = Field("supersecret", env="SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

settings = Settings()
