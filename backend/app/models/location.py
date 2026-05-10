# models/location.py
from pydantic import BaseModel
from datetime import datetime

class Location(BaseModel):
    latitude: float
    longitude: float
    timestamp: datetime
    shipment_id: int

    class Config:
        orm_mode = True
