from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from config.db import engine
from models.user import users
from schema.user import User
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

@user.get('/api/users')
def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()

        return result


@user.post('/user', status_code=HTTP_201_CREATED)
def create_user(user: User):
    with engine.connect() as conn:
        new_user = user.dict()
        new_user = {"name": user.name, "email": user.email}
        new_user["password"] = f.encrypt(user.password.encode("utf-8"))
        result = conn.execute(users.insert().values(new_user))
        conn.commit()
        print(result)
        return Response(status_code=HTTP_201_CREATED)


@user.get('/users')
def helloworld():
    return "hello world 2"
