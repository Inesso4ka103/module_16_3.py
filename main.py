from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def post_user(
    username: Annotated[str, Path(min_length=5, max_length=20,discription='Enter username')],
    age: Annotated[int, Path(ge=18, le=120, discription='Enter age')]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f'User {current_index} is updated'

@app.put('/user/{user_id}/{username}/{age}')
async def put_user(
    user_id: Annotated[int, Path(ge=0,le=100, discription='Enter User ID')],
    username: Annotated[str, Path(min_length=5, max_length=20,discription='Enter username')],
    age: Annotated[int, Path(ge=18, le=120, discription='Enter age')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

@app.delete('/users/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=0,le=100, discription='Enter User ID')]) -> str:
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'