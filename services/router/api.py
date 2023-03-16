from fastapi import APIRouter

from api.v1.endpoints import agente

api_router = APIRouter()

api_router.include_router(agente.router, prefix='/agentes', tags=['agentes'])