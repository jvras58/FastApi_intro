from fastapi import FastAPI, HTTPException

from app.schema import Message, UserList, UserPublic, UserSchema, userDB

app = FastAPI()


database = []


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = userDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User not found')
    database[user_id - 1] = userDB(**user.model_dump(), id=user_id)
    return database[user_id - 1]


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User not found')
    database.pop(user_id - 1)
    return {'detail': 'User deleted successfully'}
