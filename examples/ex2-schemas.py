from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


# Base de dados utilizado
class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


# Modelo de retorno ao usuario adotado
# a 'password' não será retornada por questões de boas práticas de segurança
class UserPublic(BaseModel):
    username: str
    email: EmailStr
