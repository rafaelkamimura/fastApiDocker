from pydantic import BaseSettings
class Settings(BaseSettings):
    userPrefix: str = '/apisUsuario'
    class Config: 
        case_sensitive = True
    

settings: Settings = Settings()