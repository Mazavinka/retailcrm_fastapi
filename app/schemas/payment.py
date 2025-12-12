from pydantic import BaseModel
from typing import Optional


class CreatePayment(BaseModel):
    order_id: int
    amount: float
    type: Optional[str] = "cash"
