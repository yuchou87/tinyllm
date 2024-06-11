import os

from pydantic import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings(BaseSettings):
    class Config:
        env_file = f'{BASE_DIR}/.env'
        env_file_encoding = 'utf-8'
