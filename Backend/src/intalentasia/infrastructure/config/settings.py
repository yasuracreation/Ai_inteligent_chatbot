from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    pinecone_api_key: str = Field(..., env="PINECONE_API_KEY")
    pinecone_index_name: str = Field(..., env="PINECONE_INDEX_NAME")
    langsmith_tracing: bool = Field(..., env="LANGSMITH_TRACING")
    langsmith_api_key: str = Field(..., env="LANGSMITH_API_KEY")
    langsmith_project: str = Field(..., env="LANGSMITH_PROJECT")
    jwt_secret_key: str = Field(..., env="JWT_SECRET_KEY")
    api_host: str = Field(..., env="API_HOST")
    api_port: int = Field(..., env="API_PORT")
    streamlit_api_url: str = Field(..., env="STREAMLIT_API_URL")
    openai_model_supervisor: str = Field(..., env="OPENAI_MODEL_SUPERVISOR")
    openai_model_worker: str = Field(..., env="OPENAI_MODEL_WORKER")
    embedding_model: str = Field(..., env="EMBEDDING_MODEL")
    rate_limit_requests_per_minute: int = Field(..., env="RATE_LIMIT_REQUESTS_PER_MINUTE")

@lru_cache
def get_settings() -> Settings:
    return Settings()