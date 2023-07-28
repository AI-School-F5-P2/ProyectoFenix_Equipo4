from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.professors_schema import ProfessorSchema
from config.db import engine
from model.professors import professors
from typing import List
from logger.logger import log_critical, log_info, log_error

professor_router = APIRouter()


@professor_router.get("/api/professors", tags=["professors"], response_model=List[ProfessorSchema])
def get_professors():
    try:
        with engine.connect() as conn:
            result = conn.execute(professors.select()).fetchall()
            log_info("Trae todos los profesores con exito")
        return result
    except Exception as e:
        log_critical(f"Error while getting professors: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@professor_router.get("/api/professors/{professor_id}",tags=["professors"], response_model=ProfessorSchema)
def get_professor(professor_id: int):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                professors.select().where(professors.c.id_prof == professor_id)
            ).first()
            log_info("Conexion correcta para buscar un profesor exacto")
        if result is None:
            log_error("Profesor no encontrado")
            raise HTTPException(status_code=404, detail="Professor not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        log_critical(f"Error while getting professor: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@professor_router.post("/api/professors", tags=["professors"],status_code=HTTP_201_CREATED)
def create_professor(professor_data: ProfessorSchema):
    try:
        with engine.connect() as conn:
            new_professor = professor_data.dict()
            conn.execute(professors.insert().values(new_professor))
            log_info("Profesor creado con exito ")
        return {"message": "Professor created successfully"}
    except Exception as e:
        log_critical(f"Error while creating professor: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@professor_router.put(
    "/api/professors/{professor_id}", tags=["professors"],response_model=ProfessorSchema
)
def update_professor(professor_data: ProfessorSchema, professor_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(
                professors.update().values(professor_data).where(
                    professors.c.id_prof == professor_id
                )
            )
            updated_professor = conn.execute(
                professors.select().where(professors.c.id_prof == professor_id)
            ).first()
            log_info("Profesor actualizado con exito")
        return updated_professor
    except Exception as e:
        log_critical(f"Error while updating professor: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@professor_router.delete(
    "/api/professors/{professor_id}",tags=["professors"], status_code=HTTP_204_NO_CONTENT
)
def delete_professor(professor_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(professors.delete().where(professors.c.id_prof == professor_id))
            log_info("Profesor eliminado con exito")
        return {"message": "Professor deleted successfully"}
    except Exception as e:
        log_critical(f"Error while deleting professor: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")