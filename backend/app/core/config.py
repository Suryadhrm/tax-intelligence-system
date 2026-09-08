from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Tax Intelligence System API"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    DATABASE_URL: str = "postgresql://tis_user:tis_password@localhost:5432/tax_intelligence_db"
    SECRET_KEY: str = "change-this-to-a-random-secret-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    PBJT_TAX_RATE: float = 0.10
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @model_validator(mode="after")
    def _validate_production(self):
        insecure_defaults = {"change-this-to-a-random-secret-in-production", "secret", "changeme", ""}
        is_prod = self.ENVIRONMENT.lower() in {"production", "prod"}
        if is_prod:
            if self.DEBUG:
                raise ValueError("DEBUG must be false in production")
            if self.SECRET_KEY.strip() in insecure_defaults or len(self.SECRET_KEY.strip()) < 32:
                raise ValueError("SECRET_KEY must be set to a strong random value in production (>=32 chars)")
        else:
            if self.SECRET_KEY.strip() in insecure_defaults and len(self.SECRET_KEY.strip()) < 32:
                pass
        return self


settings = Settings()
