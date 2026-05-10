"""
FastAPI router for shipment endpoints.
"""
from fastapi import APIRouter, HTTPException, status
from app.models.shipment import Shipment
from app.services.shipment_service import ShipmentService

router = APIRouter()

@router.post("/", response_model=Shipment, status_code=status.HTTP_201_CREATED)
async def create_shipment(shipment: Shipment):
    try:
        created = ShipmentService.create_shipment(shipment)
        return created
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
