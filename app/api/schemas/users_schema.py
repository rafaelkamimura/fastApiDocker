from pydantic import BaseModel


class UserBase(BaseModel):
    cpf: str
    nome: str
    email: str
    telefone: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True