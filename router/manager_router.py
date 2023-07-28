from fastapi import APIRouter, HTTPException, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.manager_schema import ManagerSchema
from config.db import engine
from model.manager import manager
from typing import List
from logger.logger import log_critical, log_info, log_error

manager_router = APIRouter()


@manager_router.get("/api/managers", tags=["manager"], response_model=List[ManagerSchema])
def get_managers():
    try:
        with engine.connect() as conn:
            result = conn.execute(manager.select()).fetchall()
            log_info("managers traidos con exito")
        return result
    except Exception as e:
        log_critical(f"Error while getting managers: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@manager_router.get("/api/managers/{manager_id}", tags=["manager"], response_model=ManagerSchema)
def get_manager(manager_id: int):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                manager.select().where(manager.c.id_mana == manager_id)
            ).first()
            log_info("Trae el manager con exito")
        if result is None:
            log_error("no encontrado el manager")
            raise HTTPException(status_code=404, detail="Manager not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        log_critical(f"Error while getting manager: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@manager_router.post("/api/managers", tags=["manager"], status_code=HTTP_201_CREATED)
def create_manager(manager_data: ManagerSchema):
    try:
        with engine.connect() as conn:
            new_manager = manager_data.dict()
            conn.execute(manager.insert().values(new_manager))
            log_info("Manager creado con exito")
        return Response(status_code=HTTP_201_CREATED)
    except Exception as e:
        log_critical(f"Error while creating manager: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@manager_router.put("/api/managers/{manager_id}", tags=["manager"], response_model=ManagerSchema)
def update_manager(manager_data: ManagerSchema, manager_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(
                manager.update().values(manager_data).where(
                    manager.c.id_mana == manager_id
                )
            )
            updated_manager = conn.execute(
                manager.select().where(manager.c.id_mana == manager_id)
            ).first()
            log_info("Actualizacion de manager con exito")
        return updated_manager
    except Exception as e:
        log_critical(f"Error while updating manager: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@manager_router.delete("/api/managers/{manager_id}", tags=["manager"], status_code=HTTP_204_NO_CONTENT)
def delete_manager(manager_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(manager.delete().where(manager.c.id_mana == manager_id))
            log_info("Manager eliminado correctamente")
        return Response(status_code=HTTP_204_NO_CONTENT)
    except Exception as e:
        log_critical(f"Error while deleting manager: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")
