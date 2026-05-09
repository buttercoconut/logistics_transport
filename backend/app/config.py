# config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/logistics"
    GOOGLE_MAPS_API_KEY: str = "YOUR_GOOGLE_MAPS_API_KEY"
    class Config:
        env_file = ".env"

settings = Settings()
