from pydantic import BaseModel, EmailStr, ConfigDict


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserSchema(UserPublic):
    password: str


class UserList(BaseModel):
    users: list[UserPublic]


class userDB(UserPublic):
    id: int


class Message(BaseModel):
    detail: str
