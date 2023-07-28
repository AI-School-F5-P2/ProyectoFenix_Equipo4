from fastapi import APIRouter, HTTPException
from sqlalchemy import select, update
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.class_schema import ClassSchema
from config.db import engine
from model.classes import classes
from typing import List
from logger.logger import log_critical, log_error, log_info

classes_router = APIRouter()


@classes_router.get("/api/classes", tags=["class"], response_model=List[ClassSchema])
def get_classes():
    try:
        with engine.connect() as conn:
            result = conn.execute(classes.select()).fetchall()
            log_info("Clases traidas con exito")
        return result
    except Exception as e:
        log_critical(f"Error while getting classes: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@classes_router.get("/api/classes/{class_id}", tags=["class"], response_model=ClassSchema)
def get_class(class_id: int):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                classes.select().where(classes.c.id_class == class_id)
            ).first()
            log_info("Clase traida con exito")
        if result is None:
            log_error("Clase inexistente")
            raise HTTPException(status_code=404, detail="Class not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        log_critical(f"Error while getting class: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@classes_router.post("/api/classes", tags=["class"], status_code=HTTP_201_CREATED)
def create_class(class_data: ClassSchema):
    try:
        with engine.connect() as conn:
            new_class = class_data.dict()
            conn.execute(classes.insert().values(new_class))
            log_info("Clase creada con exito")
        return {"message": "Class created successfully"}
    except Exception as e:
        log_critical(f"Error while creating class: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@classes_router.put("/api/classes/{class_id}", tags=["class"], response_model=ClassSchema)
def update_class(class_data: ClassSchema, class_id: int):
    try:
        updated_data = class_data.dict()
        with engine.connect() as conn:
            conn.execute(
                classes.update().values(**updated_data).where(classes.c.id_class == class_id)
            )
            updated_class = conn.execute(
                classes.select().where(classes.c.id_class == class_id)
            ).first()
            log_info("clase actualizada con exito")
        return updated_class
    except Exception as e:
        log_critical(f"Error while updating class: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@classes_router.delete("/api/classes/{class_id}", tags=["class"], status_code=HTTP_204_NO_CONTENT)
def delete_class(class_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(classes.delete().where(classes.c.id_class == class_id))
            log_info("Clase eliminida con exito")
        return {"message": "Class deleted successfully"}
    except Exception as e:
        log_critical(f"Error while deleting class: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@classes_router.put("/api/classes/{class_id}/assign_professor/{professor_id}", tags=["class"])
def assign_professor_to_class(class_id: int, professor_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(
                classes.update()
                .values(professor_id=professor_id)
                .where(classes.c.id_class == class_id)
            )
            log_info("clase asignada al profesor con exito")
        return {"message": "Professor assigned to class successfully"}
    except Exception as e:
        log_critical(f"Error while assigning professor to class: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")