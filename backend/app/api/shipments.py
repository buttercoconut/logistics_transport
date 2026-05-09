# api/shipments.py
from fastapi import APIRouter, Depends
from typing import List
from ..services.shipment_service import create_shipment, list_shipments
from ..models.shipment import ShipmentCreate, Shipment

router = APIRouter()

@router.post("/", response_model=Shipment)
async def create_shipment_endpoint(shipment: ShipmentCreate):
    return await create_shipment(shipment)

@router.get("/", response_model=List[Shipment])
async def list_shipments_endpoint():
    return await list_shipments()
