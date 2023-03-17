import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from sqlalchemy.ext.declarative import declarative_base
from app.db.base import database, metadata, engine
from app.config.settings import settings
from app.api.routes.users_routes import user_router

saBase = declarative_base()

app = FastAPI(title='Backend Processo Seletivo Codhab - Rafael')
userPrefix = settings.userPrefix
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database connection
@app.on_event("startup")
async def startup():
    await database.connect()
#Criar todas as tabelas:
# async def create_all_tables():
    async with engine.begin() as conn:
        print("Creating tables...")
        try:
            await conn.run_sync(saBase.metadata.create_all)
            return print('Done!')
        except Exception as e:
            print(e)
        # asyncio.run(create_all_tables())


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Rotas
app.include_router(user_router, prefix=userPrefix, tags=['CRUD Usuário'])

# Api Collection
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="APIs Collection",
        version="0.1.0",
        description="Processo Seletivo CODHAB",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


@app.get("/jsonCollection/", description='API Json Collection', tags=['JSON Collection'])
async def get_open_api_endpoint():
    return JSONResponse(content=custom_openapi())

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host= "0.0.0.0", port=8000, log_level='info', reload=True)