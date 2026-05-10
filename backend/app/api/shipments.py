# api/shipments.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models.shipment import ShipmentCreate, Shipment
from ..services.shipment_service import create_shipment, get_shipment, list_shipments

router = APIRouter(prefix="/shipments", tags=["shipments"])

@router.post("", response_model=Shipment)
async def create_shipment_endpoint(shipment_in: ShipmentCreate):
    try:
        shipment = await create_shipment(shipment_in)
        return shipment
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=List[Shipment])
async def list_shipments_endpoint():
    return await list_shipments()

@router.get("/{shipment_id}", response_model=Shipment)
async def get_shipment_endpoint(shipment_id: int):
    shipment = await get_shipment(shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment
