from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: str = Field(default="development", alias="APP_ENV")
    app_name: str = Field(default="SocialMedia Insights API", alias="APP_NAME")
    api_prefix: str = Field(default="/api/v1", alias="API_PREFIX")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    allowed_origins: list[str] = Field(default=["http://localhost:3000"], alias="ALLOWED_ORIGINS")

    supabase_url: str = Field(default="https://example.supabase.co", alias="SUPABASE_URL")
    supabase_anon_key: str = Field(default="anon-key", alias="SUPABASE_ANON_KEY")
    supabase_jwt_secret: str = Field(default="dev-secret", alias="SUPABASE_JWT_SECRET")

    gcp_project_id: str = Field(default="demo-project", alias="GCP_PROJECT_ID")
    gcp_location: str = Field(default="us-central1", alias="GCP_LOCATION")
    vertex_model: str = Field(default="gemini-1.5-pro", alias="VERTEX_MODEL")

    rate_limit: str = Field(default="60/minute", alias="RATE_LIMIT")


settings = Settings()
