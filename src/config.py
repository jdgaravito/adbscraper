from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    '''This class will contain the settings for the application.'''
    POSTGRES_URL: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

