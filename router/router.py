
from fastapi import APIRouter, Response, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schema.user_schema import UserSchema, DataUser
from config.db import engine
from model.users import users
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from tags import tags_metadata
from logger.logger import log_critical, log_debug, log_error, log_info, log_warning
from sqlalchemy import text
from config.config import settings

user = APIRouter()


@user.get("/")
def root():
    try:
        with engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {settings.MYSQL_DB};"))
            log_info("Inicio de la Api correcto")
        return {"Message": "Soy Api con Router"}
    except:
        log_critical("No se pudo establecer conexion")

@user.get("/api/user", tags=["users"], response_model=List[UserSchema])
def get_users():
    try:
        with engine.connect() as conn:
            result = conn.execute(users.select()).fetchall()
            log_info("conexion correcta para la solicitud de la lista de usuarios")
        return result
    except Exception as e:
        log_error("No se pudo mostrar la lista de usuarios")
        raise HTTPException(status_code=500, detail="Something went wrong")
        

@user.get("/api/user/{user_id}", tags=["users"], response_model=UserSchema)
def get_user(user_id: str):
    try:
        with engine.connect() as conn:
            result = conn.execute(users.select().where(users.c.id_user == user_id)).first()
            log_info("conexion correcta en la solicitud de muestra de usuario especifico")
        if result is None:
            log_warning("no existe el usuario")
            raise HTTPException(status_code=404, detail="User not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        log_error("Ha ocurrido un error en la busqueda del usuario especifico")
        raise HTTPException(status_code=500, detail="Something went wrong")


@user.post("/api/user", tags=["users"], status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    try:
        with engine.connect() as conn:
            new_user = data_user.dict()
            new_user["password"] = generate_password_hash(data_user.password, "pbkdf2:sha256:30", 30)
            conn.execute(users.insert().values(new_user))
            log_info("conexion correcta en la solicitud de agregar un usuario nuevo")

        return Response(status_code=HTTP_201_CREATED)
    except Exception as e:
        log_error("Ha ocurrido un error a subir el nuevo usuario")
        raise HTTPException(status_code=500, detail="Something went wrong")


@user.post("/api/user/login", tags=["users"], status_code=200)
def user_login(data_user: DataUser):
    try:
        with engine.connect() as conn:
            result = conn.execute(users.select().where(users.c.type_user == data_user.type_user)).first()
            log_info("conexion correcta para accesos de usuario")
            if result is not None:
                check_password = check_password_hash(result[2], data_user.password)
                if check_password:
                    log_info("Usuario correcto, acceso aprobado")
                    return {
                        "status": 200,
                        "message": "Access success"
                    }
        log_info("El usuario no tiene acceso")
        return {
            "status": HTTP_401_UNAUTHORIZED,
            "message": "Access denied"
        }
    except Exception as e:
        log_error("Ha ocurrido un error para acceder al usuario")
        raise HTTPException(status_code=500, detail="Something went wrong")


@user.put("/api/user/{user_id}", tags=["users"], response_model=UserSchema)
def update_user(data_update: UserSchema, user_id: str):
    try:
        with engine.connect() as conn:
            encryp_password = generate_password_hash(data_update.password, "pbkdf2:sha256:30", 30)
            conn.execute(users.update().values(id_user=data_update.id_user, type_user=data_update.type_user,
                                                password=encryp_password).where(users.c.id_user == user_id))
            result = conn.execute(users.select().where(users.c.id_user == user_id)).first()
            log_info("conexion correcta para la actualizacion de usuario especifico")
        return result
    except Exception as e:
        log_error("Ocurrio un error para poder actualizar el usuario seleccionado")
        raise HTTPException(status_code=500, detail="Something went wrong")


@user.delete("/api/user/{user_id}", tags=["users"], status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    try:
        with engine.connect() as conn:
            conn.execute(users.delete().where(users.c.id_user == user_id))
            log_info("conexion correcta para la eliminacion de usuario especifico")
        return Response(status_code=HTTP_204_NO_CONTENT)
    except Exception as e:
        log_error("Ha ocurrido un error para poder eliminar el usuario solicitado")
        raise HTTPException(status_code=500, detail="Something went wrong")