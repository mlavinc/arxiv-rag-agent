from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Centralized application settings.
    Values are loaded from environment variables or a .env file."""

    PROJECT_NAME: str = "ArXiv RAG Agent"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=True)

settings = Settings()