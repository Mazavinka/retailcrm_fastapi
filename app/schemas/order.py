from pydantic import BaseModel
from typing import Optional


class OrderItem(BaseModel):
    name: str
    price: float
    quantity: int


class CreateOrder(BaseModel):
    order_number: str
    customer_id: int
    items: list[OrderItem]
