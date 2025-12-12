import json
import httpx
from dotenv import load_dotenv
from app.schemas.customer import Customer
from app.schemas.order import CreateOrder
from app.schemas.payment import CreatePayment
import os
from fastapi import HTTPException

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("RETAILCRM_API_KEY")
HEADERS = {"X-API-KEY": API_KEY}


class RetailAPI:

    @staticmethod
    async def create_customers(customer: Customer):
        payload = {
            "firstName": customer.firstName,
            "lastName": customer.lastName,
            "email": customer.email,
            "phones": [{"number": customer.phone}]
        }
        customer_payload = {k: v for k, v in payload.items() if v is not None}
        payload = {
            "customer": json.dumps(customer_payload)
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(f"{BASE_URL}/api/v5/customers/create", headers=HEADERS, data=payload)

        except httpx.RequestError as e:
            raise HTTPException(status_code=502, detail=f"RetailCRM is unavailable: {str(e)}")

        if response.status_code >= 400:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        return response.json()

    @staticmethod
    async def list_customers(name: str | None = None,
                             email: str | None = None,
                             created_at: str | None = None):
        payload = {
            "filter[name]": name,
            "filter[email]": email,
            "filter[createdAtFrom]": created_at
        }
        payload = {k: v for k, v in payload.items() if v}
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{BASE_URL}/api/v5/customers", headers=HEADERS, params=payload)

        except httpx.RequestError as e:
            raise HTTPException(status_code=502, detail=f"RetailCRM is unavailable: {str(e)}")

        if response.status_code >= 400:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        return response.json()

    @staticmethod
    async def get_orders_by_customers_id(customer_id: int):
        payload = {"filter[customerId]": customer_id}

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{BASE_URL}/api/v5/orders", headers=HEADERS, params=payload)

        except httpx.RequestError as e:
            raise HTTPException(status_code=502, detail=f"RetailCRM is unavailable: {str(e)}")

        if response.status_code >= 400:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        return response.json()

    @staticmethod
    async def create_new_order(order: CreateOrder):
        payload = {
            "number": order.order_number,
            "customer": {
                "id": order.customer_id
            },
            "items": [{
                "offer": {"name": item.name},
                "quantity": item.quantity,
                "initialPrice": item.price,
            } for item in order.items
            ]
        }
        payload = {"order": json.dumps(payload)}

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(f"{BASE_URL}/api/v5/orders/create", headers=HEADERS, data=payload)

        except httpx.RequestError as e:
            raise HTTPException(status_code=502, detail=f"RetailCRM is unavailable: {str(e)}")

        if response.status_code >= 400:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        return response.json()

    @staticmethod
    async def create_payment(payment: CreatePayment):
        payload = {
            "order": {"id": payment.order_id},
            "amount": payment.amount,
            "type": payment.type
        }
        payload = {"payment": json.dumps(payload)}

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(f"{BASE_URL}/api/v5/orders/payments/create", headers=HEADERS, data=payload)

        except httpx.RequestError as e:
            raise HTTPException(status_code=502, detail=f"RetailCRM is unavailable: {str(e)}")

        if response.status_code >= 400:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        return response.json()
