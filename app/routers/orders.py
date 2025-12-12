from fastapi import APIRouter
from app.services.retailcrm import RetailAPI
from app.schemas.order import CreateOrder

router = APIRouter(prefix="/orders")


@router.get("/")
async def get_orders_by_customer_id(customer_id: int):
    result = await RetailAPI.get_orders_by_customers_id(customer_id)
    return result


@router.post("/")
async def create_order(order: CreateOrder):
    result = await RetailAPI.create_new_order(order)
    return result

