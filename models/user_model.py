from ormar import Model, StringField, IntegerField, UUIDField, BooleanField, DateTimeField, ForeignKey
from uuid import UUID

class User(Model):
    class Meta:
        tablename = "users"
        database = conn

    id: UUIDField = UUIDField(primary_key=True, default=UUID, uuid_format='hex')
    cpf: StringField = StringField(max_length=14, unique=True)
    name: StringField = StringField(max_length=100)
    email: StringField = StringField(max_length=100, unique=True)
    phone: StringField = StringField(max_length=20)