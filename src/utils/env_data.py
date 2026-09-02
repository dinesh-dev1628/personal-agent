# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    # Required — app crashes at startup if these are missing
    groq_api_key: str

    host: str
    port: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,  # GROQ_API_KEY or groq_api_key both work
    )

settings = Settings()