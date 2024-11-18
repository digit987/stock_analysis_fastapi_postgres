from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "1234"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DATABASE_NAME: str = "stocks"

    @property
    def DATABASE_URL(self) -> str:
        """Construct the database URL from the settings."""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DATABASE_NAME}"

    class Config:
        env_file = ".env"

settings = Settings()
