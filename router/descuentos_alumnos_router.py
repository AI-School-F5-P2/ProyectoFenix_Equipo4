from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.descuentos_alumnos_schema import DescuentoAlumnoSchema
from config.db import engine
from model.descuentos_alumnos import descuentos_alumnos
from typing import List

descuentos_alumnos_router = APIRouter()


@descuentos_alumnos_router.get("/api/descuentos_alumnos", tags=["discounts"], response_model=List[DescuentoAlumnoSchema])
def get_descuentos_alumnos():
    with engine.connect() as conn:
        result = conn.execute(descuentos_alumnos.select()).fetchall()

        return result


@descuentos_alumnos_router.get("/api/descuentos_alumnos/{descuento_alumno_id}",tags=["discounts"], response_model=DescuentoAlumnoSchema)
def get_descuento_alumno(descuento_alumno_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            descuentos_alumnos.select().where(descuentos_alumnos.c.id_discount_student == descuento_alumno_id)
        ).first()

        return result


@descuentos_alumnos_router.post("/api/descuentos_alumnos", tags=["discounts"], status_code=HTTP_201_CREATED)
def create_descuento_alumno(descuento_alumno_data: DescuentoAlumnoSchema):
    with engine.connect() as conn:
        new_descuento_alumno = descuento_alumno_data.dict()
        conn.execute(descuentos_alumnos.insert().values(new_descuento_alumno))

        return Response(status_code=HTTP_201_CREATED)


@descuentos_alumnos_router.put("/api/descuentos_alumnos/{descuento_alumno_id}", tags=["discounts"], response_model=DescuentoAlumnoSchema)
def update_descuento_alumno(descuento_alumno_data: DescuentoAlumnoSchema, descuento_alumno_id: int):
    with engine.connect() as conn:
        conn.execute(
            descuentos_alumnos.update().values(descuento_alumno_data).where(
                descuentos_alumnos.c.id_discount_student == descuento_alumno_id
            )
        )

        updated_descuento_alumno = conn.execute(
            descuentos_alumnos.select().where(descuentos_alumnos.c.id_discount_student == descuento_alumno_id)
        ).first()

        return updated_descuento_alumno


@descuentos_alumnos_router.delete("/api/descuentos_alumnos/{descuento_alumno_id}", tags=["discounts"], status_code=HTTP_204_NO_CONTENT)
def delete_descuento_alumno(descuento_alumno_id: int):
    with engine.connect() as conn:
        conn.execute(descuentos_alumnos.delete().where(descuentos_alumnos.c.id_discount_student == descuento_alumno_id))

        return Response(status_code=HTTP_204_NO_CONTENT)
