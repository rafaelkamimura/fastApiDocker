import databases
import ormar
import sqlalchemy

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

DATABASE_URL = "postgres://postgres:postgrespw@localhost:32768"
SA_DATABASE_URL = "postgresql+asyncpg://postgres:postgrespw@localhost:32768"
engine: AsyncEngine = create_async_engine(SA_DATABASE_URL)
saBase = declarative_base()
metadata = sqlalchemy.MetaData()
database = databases.Database(DATABASE_URL)


