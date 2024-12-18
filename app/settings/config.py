from typing import Literal

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Optional


class DatabaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="DATABASE",
        extra="ignore"
    )

    host: Optional[str] = Field(alias='DATABASE_HOST', default=None)
    port: Optional[int] = Field(alias='DATABASE_PORT', default=None)
    user: Optional[str] = Field(alias='DATABASE_USER', default=None)
    password: Optional[str] = Field(alias='DATABASE_PASSWORD', default=None)
    name: str = Field(alias='DATABASE_NAME')
    dialect: str = Field(alias='DATABASE_DIALECT')
    driver: str = Field(alias='DATABASE_DRIVER')

    @property
    @computed_field
    def url(self) -> str:
        if self.dialect == 'sqlite':
            return '{}+{}:///{}'.format(
                self.dialect,
                self.driver,
                self.name
            )
        return '{}+{}://{}:{}@{}:{}/{}'.format(
            self.dialect,
            self.driver,
            self.user,
            self.password,
            self.host,
            self.port,
            self.name
        )


class SQLAlchemyConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="ALCHEMY",
        extra="ignore"
    )

    pool_pre_ping: bool
    pool_recycle: int
    echo: bool
    auto_flush: bool
    expire_on_commit: bool


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore"
    )

    log_level: Literal["DEV", "INFO", "ERROR"] = Field(alias='LOG_LEVEL')

    database: DatabaseConfig = DatabaseConfig()
    alchemy: SQLAlchemyConfig = SQLAlchemyConfig()


config: Config = Config()
