from fastapi import APIRouter
from app.schemas.payment import CreatePayment
from app.services.retailcrm import RetailAPI

router = APIRouter(prefix="/payments")


@router.post("/")
async def create_payments(payment: CreatePayment):
    result = await RetailAPI.create_payment(payment)
    return result


