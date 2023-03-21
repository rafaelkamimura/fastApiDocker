from fastapi import APIRouter, HTTPException
from typing import List
from db.users_model import User
from api.schemas.users_schema import UserCreate, UserUpdate

user_router = APIRouter()


@user_router.post("/create", response_model=User, description='Criar Usuário', summary='Create Usuário')
async def create_user(user: UserCreate):
    new_user = await User.objects.create(**user.dict(exclude_unset=True))
    return new_user


@user_router.get("/", response_model=List[User], description='Listar todos os Usuários', summary='Read Usuários')
async def read_users():
    users = await User.objects.all()
    return users


@user_router.get("/{user_id}", response_model=User, description='Buscar usuário por ID',  summary='Read one Usuário')
async def read_user(user_id: int):
    user = await User.objects.get_or_none(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user


@user_router.put("/{user_id}", response_model=User, description='Atualizar dados de um usuário', summary='Update one Usuário')
async def update_user(user_id: int, user: UserUpdate):
    current_user = await User.objects.get_or_none(id=user_id)
    if current_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    updated_user = user.dict(exclude_unset=True)
    for field in updated_user:
        setattr(current_user, field, updated_user[field])
    await current_user.update()
    return current_user


@user_router.delete("/{user_id}", response_model=None, description='Deletar um usuário', summary='Delete one Usuário')
async def delete_user(user_id: int):
    user = await User.objects.get_or_none(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    await user.delete()
