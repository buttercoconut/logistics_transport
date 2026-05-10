"""
Configuration settings using Pydantic BaseSettings.
"""
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    # Google Maps API Key
    GOOGLE_MAPS_API_KEY: str = Field(..., env="GOOGLE_MAPS_API_KEY")

    # Other settings can be added here

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instantiate settings
settings = Settings()
