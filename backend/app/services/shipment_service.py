# services/shipment_service.py
import httpx
from typing import List
from . import shipment_service
from ..models.shipment import ShipmentCreate, Shipment, Location
from ..config import settings

# Dummy in-memory store
_shipments: List[Shipment] = []
_next_id = 1

async def create_shipment(data: ShipmentCreate) -> Shipment:
    global _next_id
    # Call Google Maps Directions API for route optimization
    route = await get_optimal_route(data.origin, data.destination)
    shipment = Shipment(
        id=_next_id,
        origin=data.origin,
        destination=data.destination,
        weight_kg=data.weight_kg,
        description=data.description,
        carrier_id=data.carrier_id,
        status="scheduled",
        route=route,
    )
    _shipments.append(shipment)
    _next_id += 1
    return shipment

async def get_optimal_route(origin: Location, destination: Location) -> List[Location]:
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": f"{origin.latitude},{origin.longitude}",
        "destination": f"{destination.latitude},{destination.longitude}",
        "key": settings.GOOGLE_MAPS_API_KEY,
        "mode": "driving",
        "optimize:true": "true",
    }
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()
        if data["status"] != "OK":
            raise ValueError("Google Maps API error")
        steps = data["routes"][0]["legs"][0]["steps"]
        route = []
        for step in steps:
            lat = step["start_location"]["lat"]
            lng = step["start_location"]["lng"]
            route.append(Location(latitude=lat, longitude=lng))
        # add final destination
        route.append(destination)
        return route

async def list_shipments() -> List[Shipment]:
    return _shipments
