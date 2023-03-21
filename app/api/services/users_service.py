from typing import List
from db.users_model import User
from api.schemas.users_schema import UserCreate, UserUpdate


async def get_all_users():
    return await User.objects.all()


async def get_user(user_id: int):
    return await User.objects.get(id=user_id)


async def create_user(user: UserCreate):
    user_obj = User(**user.dict())
    await user_obj.save()
    return user_obj


async def update_user(user_id: int, user: UserUpdate):
    user_obj = await User.objects.get(id=user_id)
    await user_obj.update(**user.dict(exclude_unset=True))
    return await User.objects.get(id=user_id)


async def delete_user(user_id: int):
    user_obj = await User.objects.get(id=user_id)
    await user_obj.delete()
    return user_obj