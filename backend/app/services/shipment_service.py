# services/shipment_service.py
import httpx
from typing import List
from ..config import settings
from ..models.shipment import Location, ShipmentCreate, Shipment

# Simple in-memory store for demo purposes
shipments_db = {}
shipment_id_seq = 1

async def calculate_optimal_route(origin: Location, destination: Location) -> List[Location]:
    """Call Google Maps Directions API to get optimal route."""
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": f"{origin.latitude},{origin.longitude}",
        "destination": f"{destination.latitude},{destination.longitude}",
        "key": settings.GOOGLE_MAPS_API_KEY,
        "mode": "driving",
    }
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()
        if data.get("status") != "OK":
            raise ValueError("Google Maps API error: " + data.get("status"))
        # Extract polyline points
        steps = data["routes"][0]["legs"][0]["steps"]
        route = []
        for step in steps:
            start_loc = step["start_location"]
            route.append(Location(latitude=start_loc["lat"], longitude=start_loc["lng"], timestamp=None))
        # Add destination
        dest = data["routes"][0]["legs"][0]["end_location"]
        route.append(Location(latitude=dest["lat"], longitude=dest["lng"], timestamp=None))
        return route

async def create_shipment(shipment_in: ShipmentCreate) -> Shipment:
    global shipment_id_seq
    route = await calculate_optimal_route(shipment_in.origin, shipment_in.destination)
    shipment = Shipment(
        id=shipment_id_seq,
        origin=shipment_in.origin,
        destination=shipment_in.destination,
        weight_kg=shipment_in.weight_kg,
        description=shipment_in.description,
        carrier_id=shipment_in.carrier_id,
        status="created",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        route=route,
    )
    shipments_db[shipment_id_seq] = shipment
    shipment_id_seq += 1
    return shipment

async def get_shipment(shipment_id: int) -> Shipment:
    return shipments_db.get(shipment_id)

async def list_shipments() -> List[Shipment]:
    return list(shipments_db.values())
