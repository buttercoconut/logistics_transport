# models/driver.py
from pydantic import BaseModel

class DriverBase(BaseModel):
    name: str
    license_number: str

class DriverCreate(DriverBase):
    carrier_id: int

class Driver(DriverBase):
    id: int
    carrier_id: int

    class Config:
        orm_mode = True
