import os

from pydantic import BaseSettings, SecretStr

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings(BaseSettings):
    GROQ_API_KEY: SecretStr
    GOOGLE_API_KEY: SecretStr

    class Config:
        env_file = f'{BASE_DIR}/.env'
        env_file_encoding = 'utf-8'
