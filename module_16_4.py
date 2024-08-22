from fastapi import FastAPI, Path, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel
app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
def put_user_name_age(list_users: User, username: str, age: int) -> str:
    list_users.id = len(users) + 1
    users.append(list_users)
    list_users.username = username
    list_users.age = age
    return "Message created!"


@app.put('/user/{user_id}/{username}/{age}')
def update_users(user_id: int, username: str, age: int) -> str:
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return "Message updated."
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> list:
    try:
        users.pop(user_id)
        return users
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
