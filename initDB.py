from app.db.base import database, metadata, engine, saBase
async def create_tables() -> None:
    print('Criando as tabelas no Banco de Dados...')

    async with engine.begin() as conn:
        
        await conn.run_sync(saBase.metadata.drop_all)
        await conn.run_sync(saBase.metadata.create_all)
    
    print('Tabelas criadas com sucesso!')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())