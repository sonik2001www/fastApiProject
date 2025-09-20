import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./blog.db"
    PROJECT_NAME: str = "Blog API"
    SECRET_KEY: str = "supersecret"

settings = Settings()
