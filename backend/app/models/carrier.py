# models/carrier.py
from pydantic import BaseModel
from typing import List

class CarrierBase(BaseModel):
    name: str
    rating: float = 5.0

class CarrierCreate(CarrierBase):
    pass

class Carrier(CarrierBase):
    id: int
    drivers: List[int] = []

    class Config:
        orm_mode = True
