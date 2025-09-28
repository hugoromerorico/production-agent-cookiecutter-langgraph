from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    PydanticBaseSettingsSource,
    YamlConfigSettingsSource
)
from pydantic import BaseModel
import os
from loguru import logger


class Server(BaseModel):
    host: str
    port: int


class Settings(BaseSettings):
    # Declare the settings
    server: Server
    log_level: str

    # Necessary to load config from yaml file
    model_config = SettingsConfigDict(
        yaml_file="app/config/config.yaml",
        yaml_file_encoding="utf-8",
        extra="ignore",
        env_file=".env",
        env_file_encoding="utf-8"
    )
    @classmethod # Necesary to load config from yaml file and env
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            YamlConfigSettingsSource(settings_cls),
            dotenv_settings,
            env_settings,
        )

settings = Settings() # The accessible instance of the Settings class
logger.debug(f"Settings: {settings}")
