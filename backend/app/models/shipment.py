# models/shipment.py
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Location(BaseModel):
    latitude: float
    longitude: float
    timestamp: Optional[datetime] = None

class ShipmentBase(BaseModel):
    origin: Location
    destination: Location
    weight_kg: float
    description: Optional[str] = None

class ShipmentCreate(ShipmentBase):
    carrier_id: int

class Shipment(ShipmentBase):
    id: int
    carrier_id: int
    status: str = Field(default="created")
    created_at: datetime
    updated_at: datetime
    route: Optional[List[Location]] = None

    class Config:
        orm_mode = True
