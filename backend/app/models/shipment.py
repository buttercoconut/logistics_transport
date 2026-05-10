"""
Pydantic model for Shipment.
"""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class Location(BaseModel):
    latitude: float
    longitude: float
    timestamp: datetime

class Shipment(BaseModel):
    id: Optional[int] = Field(None, description="Shipment ID, auto-generated")
    origin: Location
    destination: Location
    carrier_id: int
    driver_id: Optional[int] = None
    status: str = Field("created", description="Current status of the shipment")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    route: Optional[List[Location]] = None
    estimated_cost: Optional[float] = None

    class Config:
        orm_mode = True
