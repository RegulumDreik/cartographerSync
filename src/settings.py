from pydantic import BaseSettings


class Settings(BaseSettings):
    """App settings."""


def get_settings() -> Settings:
    """Get settings.

    Returns:
        Settings
    """
    return Settings()


settings = get_settings()
