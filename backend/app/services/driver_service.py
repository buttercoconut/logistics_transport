# services/driver_service.py
from typing import List
from ..models.driver import Driver, DriverCreate

# In-memory store for demo
drivers_db = {}
drivers_id_seq = 1

async def create_driver(driver_in: DriverCreate) -> Driver:
    global drivers_id_seq
    driver = Driver(id=drivers_id_seq, name=driver_in.name, license_number=driver_in.license_number, carrier_id=driver_in.carrier_id)
    drivers_db[drivers_id_seq] = driver
    drivers_id_seq += 1
    return driver

async def get_driver(driver_id: int) -> Driver:
    return drivers_db.get(driver_id)

async def list_drivers() -> List[Driver]:
    return list(drivers_db.values())
