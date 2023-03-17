from ormar import Model, String, Integer
from app.db.base import database as db
from app.db.base import metadata as dbmetadata
class User(Model):
    class Meta:
        tablename = "users"
        database= db
        metadata = dbmetadata
        
    id: int = Integer(primary_key=True)
    cpf: str = String(max_length=11, unique=True, index=True)
    name: str = String(max_length=50)
    email: str = String(max_length=50, unique=True)
    phone: str = String(max_length=20)