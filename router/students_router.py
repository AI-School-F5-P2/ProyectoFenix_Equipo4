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
import logging
import pprint

student_router = APIRouter()


@student_router.get("/api/students", response_model=List[StudentSchema])
def get_students():
    with engine.connect() as conn:
        result = conn.execute(students.select()).fetchall()

        return result


@student_router.get("/api/students/{student_id}", response_model=StudentSchema)
def get_student(student_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            students.select().where(students.c.id_student == student_id)
        ).first()

        return result


@student_router.post("/api/students", status_code=HTTP_201_CREATED)
def create_student(student_data: StudentSchema):
    with engine.connect() as conn:
        new_student = student_data.dict()
        conn.execute(students.insert().values(new_student))

        return {"message": "Student created successfully"}


@student_router.put("/api/students/{student_id}", response_model=StudentSchema)
def update_student(student_data: StudentSchema, student_id: int):
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


@student_router.delete("/api/students/{student_id}", status_code=HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    with engine.connect() as conn:
        conn.execute(students.delete().where(students.c.id_student == student_id))

        return {"message": "Student deleted successfully"}



@student_router.put("/api/students/{student_id}/update_student_price/", response_model=StudentSchema)
def update_student_price(student_id: int):
     # Calcular el nuevo precio total con descuentos para el estudiante
    new_total_price = calculate_student_total_price(student_id)
    logging.info(f"El precio es: {new_total_price}")
    with engine.connect() as conn:
        # Actualizar el precio total del estudiante en la tabla 'students'
        stmt = update(students).where(students.c.id_user == student_id).values(Total_price=new_total_price)
        conn.execute(stmt)
        logging.info("guarda precio")
        # Devuelve el estudiante actualizado
        updated_student = conn.execute(select([students]).where(students.c.id_user == student_id)).first()
        # Convertir el objeto a una instancia de StudentSchema
        logging.info(updated_student)
        #updated_student_schema = StudentSchema(**updated_student)
        return updated_student
