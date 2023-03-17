from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
cstr = "postgresql+asyncpg://postgres:postgrespw@localhost:32768"
engine: AsyncEngine = sa.create_engine(cstr)
Base = declarative_base()
async def create_tables() -> None:
    metadata = sa.MetaData()
    from app.db.users_model import User
    print('Criando as tabelas no Banco de Dados...')

    async with engine.begin() as conn:
        async with engine.begin() as conn:
            await User.create_table()
            await conn.run_sync(metadata.create_all)
    print('Tabelas criadas com sucesso!')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())