from pydantic import BaseModel, EmailStr


class UserPublic(BaseModel):
    username: str
    email: EmailStr


class UserSchema(UserPublic):
    password: str


class UserList(BaseModel):
    users: list[UserPublic]


class userDB(UserPublic):
    id: int


class Message(BaseModel):
    detail: str
