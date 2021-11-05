from typing import List
from fastapi import FastAPI, HTTPException
from models import user
from crud_ops import crud
app = FastAPI()


@app.get('/')
async def index():
    return{'message': 'Welcome to FastAPI'}


@app.post('/users/', response_model=user.User)
async def create_user(_user: user.UserCreate):
    existing_user = crud.get_user_by_email(_user.email)
    # print(existing_user)
    if existing_user:
        raise HTTPException(
            status_code=400, detail=f'The email {_user.email} is already registered')
    return crud.create_user(user=_user)


@app.get('/users/', response_model=List[user.User])
async def get_users():
    users = crud.get_users()
    return users
