# api/carriers.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..models.carrier import CarrierCreate, Carrier
from ..services.carrier_service import create_carrier, get_carrier, list_carriers

router = APIRouter(prefix="/carriers", tags=["carriers"])

@router.post("", response_model=Carrier)
async def create_carrier_endpoint(carrier_in: CarrierCreate):
    carrier = await create_carrier(carrier_in)
    return carrier

@router.get("", response_model=List[Carrier])
async def list_carriers_endpoint():
    return await list_carriers()

@router.get("/{carrier_id}", response_model=Carrier)
async def get_carrier_endpoint(carrier_id: int):
    carrier = await get_carrier(carrier_id)
    if not carrier:
        raise HTTPException(status_code=404, detail="Carrier not found")
    return carrier
