import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path = env_path)

class Settings:
    PROJECT_NAME: str = "Proyectofenixdanza"
    PROJECT_VERSION: str = "1.0"
    MYSQL_DB: str = os.getenv('MYSQL_DB')
    MYSQL_USER: str = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD: str = os.getenv('MYSQL_PASSWORD')
    MYSQL_SERVER: str = os.getenv('MYSQL_SERVER')
    MYSQL_PORT: str = os.getenv('MYSQL_PORT')
    @property
    def DATABASE_URL(self):
        return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}:{self.MYSQL_PORT}/{self.MYSQL_DB}"

settings = Settings()