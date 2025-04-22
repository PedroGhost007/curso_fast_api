from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


# Herda da classe UserSchema todas as propriedades e adciona o id
class UserDB(UserSchema):
    id: int


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


# Listar os users cadastrados
class UserList(BaseModel):
    users: list[UserPublic]
