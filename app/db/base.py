import databases
import ormar
import sqlalchemy

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

DATABASE_URL = "postgresql://postgres:postgrespw@localhost/fastapi_database"
SA_DATABASE_URL = "postgresql+asyncpg://postgres:postgrespw@localhost/fastapi_database"
engine: AsyncEngine = create_async_engine(SA_DATABASE_URL)
saBase = declarative_base()
database = databases.Database(DATABASE_URL)
# metadata(bind=database)

