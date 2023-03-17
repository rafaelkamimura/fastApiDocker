from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    cpf: str
    name: str
    email: str
    phone: str


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    cpf: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None