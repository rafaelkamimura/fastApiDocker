from fastapi import APIRouter
from services.router.api import api_router
api_router = APIRouter()
api_router.include_router(api_router, prefix='/usuarios', tags=['usuarios'])