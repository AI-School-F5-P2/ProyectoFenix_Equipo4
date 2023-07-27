from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.inscriptions_schema import InscriptionSchema
from config.db import engine
from model.inscriptions import inscriptions
from model.student import students
from typing import List
from business.discount_calculator import calculate_student_total_price
from business.student_price_updater import update_student_price
from logger.logger import log_critical
from sqlalchemy import extract

inscriptions_router = APIRouter()

def log_critical(mensaje):
    # Tu código aquí para manejar la entrada de registro crítica
    print(f"CRÍTICO: {mensaje}")

@inscriptions_router.get("/api/inscriptions", response_model=List[InscriptionSchema])
def get_inscriptions():
    try:
        with engine.connect() as conn:
            result = conn.execute(inscriptions.select()).fetchall()
        return result
    except Exception as e:
        log_critical(f"Error while getting inscriptions: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@inscriptions_router.get("/api/inscriptions/{inscription_id}", response_model=InscriptionSchema)
def get_inscription(inscription_id: int):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                inscriptions.select().where(inscriptions.c.id_inscription == inscription_id)
            ).first()
        if result is None:
            raise HTTPException(status_code=404, detail="Inscription not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        log_critical(f"Error while getting inscription: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@inscriptions_router.post("/api/inscriptions", status_code=HTTP_201_CREATED)
def create_inscription(inscription_data: InscriptionSchema):
    try:
        with engine.connect() as conn:
            new_inscription = inscription_data.dict()
            conn.execute(inscriptions.insert().values(new_inscription))
            # Obtenemos el id_user (o student_id) de la inscripción
            student_id = new_inscription["id_user"]
            # Actualizamos el precio total del estudiante después de la inscripción
            # update_student_price(student_id)
        return {"message": "Inscription created successfully"}
    except Exception as e:
        log_critical(f"Error while creating inscription: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@inscriptions_router.put("/api/inscriptions/{inscription_id}", response_model=InscriptionSchema)
def update_inscription(
    inscription_data: InscriptionSchema, inscription_id: int
):
    try:
        with engine.connect() as conn:
            conn.execute(
                inscriptions.update().values(inscription_data).where(
                    inscriptions.c.id_inscription == inscription_id
                )
            )
            updated_inscription = conn.execute(
                inscriptions.select().where(
                    inscriptions.c.id_inscription == inscription_id
                )
            ).first()
        return updated_inscription
    except Exception as e:
        log_critical(f"Error while updating inscription: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@inscriptions_router.delete(
    "/api/inscriptions/{inscription_id}", status_code=HTTP_204_NO_CONTENT
)
def delete_inscription(inscription_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(
                inscriptions.delete().where(
                    inscriptions.c.id_inscription == inscription_id
                )
            )
        return {"message": "Inscription deleted successfully"}
    except Exception as e:
        log_critical(f"Error while deleting inscription: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")



@inscriptions_router.get("/api/inscriptions/by_month/{month}", response_model=List[InscriptionSchema])
def get_inscriptions_by_month(month: int):
    try:
        with engine.connect() as conn:
            # Utilizamos SQL para filtrar inscripciones por mes
            result = conn.execute(
                inscriptions.select().where(
                    extract('month', inscriptions.c.start_date) == month
                )
            ).fetchall()
        return result
    except Exception as e:
        log_critical(f"Error while getting inscriptions by month: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")