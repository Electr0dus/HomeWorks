from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def put_user_name_age(username:Annotated[str, Path(description='Enter user name', example='UrbanUser')],
                            age:Annotated[str, Path(description='Enter age user', example='25')]) -> str:
    current = str(int(max(users, key=int)) + 1)
    users[current] = f'Имя: {username}, возраст: {age}'
    return f'User {current} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id:Annotated[str, Path(description='ID user', example='1')],
                       username:Annotated[str, Path(description='Enter user name', example='UrbanUser')],
                       age:Annotated[str, Path(description='Enter age user', example='25')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id:Annotated[str, Path(description='Enter user ID', example='3')]) -> str:
    users.pop(user_id)
    return 'Delete is complete!'
