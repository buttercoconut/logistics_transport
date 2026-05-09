# models/shipment.py
from pydantic import BaseModel, Field
from typing import List, Optional

class Location(BaseModel):
    latitude: float
    longitude: float
    timestamp: Optional[str] = None

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
    route: List[Location] = Field(default_factory=list)

    class Config:
        orm_mode = True
