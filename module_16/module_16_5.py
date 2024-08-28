from fastapi import FastAPI, Path, HTTPException, Body, Request, Form
from fastapi.responses import HTMLResponse
from typing import List
from pydantic import BaseModel
from starlette import status
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')
users = []

class User(BaseModel):
    id: int
    username: str
    age: int



@app.get('/')
def send_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})

@app.get(path='/user/{user_id}')
def get_users(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id - 1]})


@app.post('/user/{username}/{age}')
def put_user_name_age(request: Request, username: str, age: int) -> HTMLResponse:
    if users:
        user_id = max(users, key=lambda u: u.id).id + 1
    else:
        user_id = 1
    users.append(User(id=user_id, username=username, age=age))
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


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
