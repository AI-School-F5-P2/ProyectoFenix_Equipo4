from fastapi import APIRouter, HTTPException
from sqlalchemy import select, update
from sqlalchemy.exc import NoResultFound
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.students_schema import StudentSchema 
from business.discount_calculator import calculate_student_total_price
from business.student_price_updater import update_student_price
from config.db import engine
from model.student import students
from typing import List
from model.descuentos_alumnos import descuentos_alumnos
from logger.logger import log_info, log_critical, log_error
import pprint

student_router = APIRouter()


@student_router.get("/api/students",tags=["students"], response_model=List[StudentSchema])
def get_students():
    try:
        with engine.connect() as conn:
            result = conn.execute(students.select()).fetchall()
            log_info("Trae con exito los estudiantes")
        return result
    except Exception as e:
        log_error(f"Error while getting students: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@student_router.get("/api/students/{student_id}", tags=["students"], response_model=StudentSchema)
def get_student(student_id: int):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                students.select().where(students.c.id_student == student_id)
            ).first()
            log_info("Conexion correcta para traer al estudiante solicitado")
        if result is None:
            log_error("Estudiante no encontrado")
            raise HTTPException(status_code=404, detail="Student not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        log_error(f"Error while getting student: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@student_router.post("/api/students",tags=["students"],  status_code=HTTP_201_CREATED)
def create_student(student_data: StudentSchema):
    try:
        with engine.connect() as conn:
            new_student = student_data.dict()
            conn.execute(students.insert().values(new_student))
            log_info("Estudiante creado con exito")
        return {"message": "Student created successfully"}
    except Exception as e:
        log_error(f"Error while creating student: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@student_router.put("/api/students/{student_id}",tags=["students"],  response_model=StudentSchema)
def update_student(student_data: StudentSchema, student_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(
                students.update().values(student_data).where(
                    students.c.id_student == student_id
                )
            )
            updated_student = conn.execute(
                students.select().where(students.c.id_student == student_id)
            ).first()
        return updated_student
    except Exception as e:
        log_error(f"Error while updating student: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@student_router.delete("/api/students/{student_id}", tags=["students"], status_code=HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(students.delete().where(students.c.id_student == student_id))
            log_info("Estudiante eliminado exitosamente")
        return {"message": "Student deleted successfully"}
    except Exception as e:
        log_error(f"Error while deleting student: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@student_router.put("/api/students/{student_id}/update_student_price/", tags=["students"], response_model=StudentSchema)
def update_student_price(student_id: int):
    try:
        # Calcular el nuevo precio total con descuentos para el estudiante
        new_total_price = calculate_student_total_price(student_id)
        log_info(f"El precio es: {new_total_price}")
        with engine.connect() as conn:
            # Actualizar el precio total del estudiante en la tabla 'students'
            stmt = update(students).where(students.c.id_user == student_id).values(Total_price=new_total_price)
            conn.execute(stmt)
            log_info("guarda precio")
            # Devuelve el estudiante actualizado
            updated_student = conn.execute(select([students]).where(students.c.id_user == student_id)).first()
        return updated_student
    except Exception as e:
        log_error(f"Error while updating student price: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")