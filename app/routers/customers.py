from fastapi import APIRouter
from app.schemas.customer import Customer
from app.services.retailcrm import RetailAPI

router = APIRouter(prefix="/customers")


@router.post("/create")
async def create_customer(customer: Customer):
    result = await RetailAPI.create_customers(customer)
    return result


@router.get("/")
async def list_customers(name: str | None = None, email: str | None = None, created_at: str | None = None):
    result = await RetailAPI.list_customers(name, email, created_at)
    return result
