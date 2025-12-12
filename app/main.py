from fastapi import FastAPI
from app.routers import customers, orders, payments

app = FastAPI()

app.include_router(customers.router)
app.include_router(orders.router)
app.include_router(payments.router)
