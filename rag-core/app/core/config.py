from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Centralized application settings.
    Values are loaded from environment variables or a .env file."""

    PROJECT_NAME: str = "ArXiv RAG Agent"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    OLLAMA_BASE_URL: str = "http://127.0.0.1:11434"
    OLLAMA_LLM_MODEL: str = "qwen2.5:3b"
    OLLAMA_EMBEDDING_MODEL: str = "nomic-embed-text"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=True)

settings = Settings()