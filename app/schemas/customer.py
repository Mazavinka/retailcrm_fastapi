from pydantic import BaseModel, EmailStr
from typing import Optional


class Customer(BaseModel):
    firstName: str
    lastName: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: str
