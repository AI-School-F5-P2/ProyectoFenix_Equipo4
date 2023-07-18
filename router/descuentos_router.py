from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.class_schema import ClassSchema
from config.db import engine
from schema.descuentos_schema import DiscountSchema
from model.descuentos import descuentos
from typing import List

descuentos_router = APIRouter()

@descuentos_router.get("/api/discounts", response_model=List[DiscountSchema])
def get_discounts():
    with engine.connect() as conn:
        result = conn.execute(descuentos.select()).fetchall()

        return result


@descuentos_router.get("/api/discounts/{discount_id}", response_model=DiscountSchema)
def get_discount(discount_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            descuentos.select().where(descuentos.c.id_discount == discount_id)
        ).first()

        return result


@descuentos_router.post("/api/discounts", status_code=HTTP_201_CREATED)
def create_discount(discount_data: DiscountSchema):
    with engine.connect() as conn:
        new_discount = discount_data.dict()
        conn.execute(descuentos.insert().values(new_discount))

        return {"message": "Discount created successfully"}


@descuentos_router.put("/api/discounts/{discount_id}", response_model=DiscountSchema)
def update_discount(discount_data: DiscountSchema, discount_id: int):
    with engine.connect() as conn:
        conn.execute(
            descuentos.update().values(discount_data).where(
                descuentos.c.id_discount == discount_id
            )
        )

        updated_discount = conn.execute(
            descuentos.select().where(descuentos.c.id_discount == discount_id)
        ).first()

        return updated_discount


@descuentos_router.delete("/api/discounts/{discount_id}", status_code=HTTP_204_NO_CONTENT)
def delete_discount(discount_id: int):
    with engine.connect() as conn:
        conn.execute(descuentos.delete().where(descuentos.c.id_discount == discount_id))

        return {"message": "Discount deleted successfully"}