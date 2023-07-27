from sqlalchemy import create_engine, MetaData
from config.config import settings

engine = create_engine(settings.DATABASE_URL, pool_size=10, max_overflow=20, pool_timeout=30)

meta_data = MetaData()