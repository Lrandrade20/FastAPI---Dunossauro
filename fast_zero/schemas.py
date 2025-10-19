from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    # O id foi adicionado pois agora fará parte do retorno
    id: int
    username: str
    email: EmailStr


# Herda todas as propriedades do UserSchema, e adiciona o id
class UserDB(UserSchema):
    id: int


# Estrutura para salvar usuarios em lista
class UserList(BaseModel):
    users: list[UserPublic]
