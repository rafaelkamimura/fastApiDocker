from sqlalchemy import MetaData
from databases import Database
import ormar
import sqlalchemy
from app.db.base import database as db
metadata = MetaData()
# class BaseMeta(ModelMeta):
#     class Meta:
#         abstract = True
class User(ormar.Model):
    class Meta:
        tablename = "users"
        database = db
        metadata = metadata
        
    id: int = ormar.Integer(primary_key=True)
    cpf: str = ormar.String(max_length=11, unique=True, index=True)
    nome: str = ormar.String(max_length=50)
    email: str = ormar.String(max_length=50, unique=True)
    telefone: str = ormar.String(max_length=20)
    
engine = sqlalchemy.create_engine(str(db.url))
metadata.create_all(engine)