from services.router.api import api_router as router
from models.user_model import User
from uuid import UUID
from fastapi.responses import JSONResponse
from ormar.exceptions import NoMatch

@router.post('/users', response_class=JSONResponse, tags=['Users'])
async def create_user(user: User):
    await user.save()
    return user.dict()

@router.put('/users/{user_id}', response_class=JSONResponse, tags=['Users'])
async def update_user(user_id: UUID, user: User):
    try:
        db_user = await User.objects.get(id=user_id)
    except NoMatch:
        return JSONResponse(content={'message': 'User not found'}, status_code=404)
    
    db_user.cpf = user.cpf
    db_user.name = user.name
    db_user.email = user.email
    db_user.phone = user.phone
    
    await db_user.update()
    
    return db_user.dict()

@router.get('/users', response_class=JSONResponse, tags=['Users'])
async def get_users():
    users = await User.objects.all()
    return [user.dict() for user in users]

@router.get('/users/{user_id}', response_class=JSONResponse, tags=['Users'])
async def get_user(user_id: UUID):
    try:
        user = await User.objects.get(id=user_id)
    except NoMatch:
        return JSONResponse(content={'message': 'User not found'}, status_code=404)
    
    return user.dict()

@router.delete('/users/{user_id}', response_class=JSONResponse, tags=['Users'])
async def delete_user(user_id: UUID):
    try:
        user = await User.objects.get(id=user_id)
    except NoMatch:
        return JSONResponse(content={'message': 'User not found'}, status_code=404)
    
    await user.delete()
    
    return JSONResponse(content={'message': 'User deleted'})
