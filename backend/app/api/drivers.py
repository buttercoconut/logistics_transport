# api/drivers.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..models.driver import DriverCreate, Driver
from ..services.driver_service import create_driver, get_driver, list_drivers

router = APIRouter(prefix="/drivers", tags=["drivers"])

@router.post("", response_model=Driver)
async def create_driver_endpoint(driver_in: DriverCreate):
    driver = await create_driver(driver_in)
    return driver

@router.get("", response_model=List[Driver])
async def list_drivers_endpoint():
    return await list_drivers()

@router.get("/{driver_id}", response_model=Driver)
async def get_driver_endpoint(driver_id: int):
    driver = await get_driver(driver_id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver
