from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT,  HTTP_500_INTERNAL_SERVER_ERROR, HTTP_404_NOT_FOUND
from schema.class_schema import ClassSchema
from config.db import engine
from schema.descuentos_schema import DiscountSchema
from model.descuentos import descuentos
from typing import List
from logger.logger import log_critical, log_info, log_error

descuentos_router = APIRouter()

@descuentos_router.get("/api/discounts", tags=["discounts"],response_model=List[DiscountSchema])
def get_discounts():
    try:
        with engine.connect() as conn:
            result = conn.execute(descuentos.select()).fetchall()
            log_info("Se trajeron los descuentos correctamente")
        return result
    except Exception as e:
        log_critical(f"Error while getting discounts: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@descuentos_router.get("/api/discounts/{discount_id}", tags=["discounts"], response_model=DiscountSchema)
def get_discount(discount_id: int):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                descuentos.select().where(descuentos.c.id_discount == discount_id)
            ).first()
            log_info("trae con exito la conexion")
        if result is None:
            log_error("No se encontro el descuento")
            raise HTTPException(status_code=404, detail="Discount not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        log_critical(f"Error while getting discount: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@descuentos_router.post("/api/discounts", tags=["discounts"], status_code=HTTP_201_CREATED)
def create_discount(discount_data: DiscountSchema):
    try:
        with engine.connect() as conn:
            new_discount = discount_data.dict()
            conn.execute(descuentos.insert().values(new_discount))
            log_info("descuento nuevo creado")
        return {"message": "Discount created successfully"}
    except Exception as e:
        log_critical(f"Error while creating discount: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@descuentos_router.put("/api/discounts/{discount_id}", tags=["discounts"], response_model=DiscountSchema)
def update_discount(discount_data: DiscountSchema, discount_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(
                descuentos.update().values(discount_data).where(
                    descuentos.c.id_discount == discount_id
                )
            )
            updated_discount = conn.execute(
                descuentos.select().where(descuentos.c.id_discount == discount_id)
            ).first()
            log_info("descuento actualizado")
        return updated_discount
    except Exception as e:
        log_critical(f"Error while updating discount: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")


@descuentos_router.delete("/api/discounts/{discount_id}",tags=["discounts"],status_code=HTTP_204_NO_CONTENT)
def delete_discount(discount_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(descuentos.delete().where(descuentos.c.id_discount == discount_id))
            log_info("descuento eliminado con exito")
        return {"message": "Discount deleted successfully"}
    except Exception as e:
        log_critical(f"Error while deleting discount: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong")
