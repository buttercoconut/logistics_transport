# api/locations.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..models.location import Location

router = APIRouter(prefix="/locations", tags=["locations"])

# For demo purposes we just store in memory
locations_db = {}
location_id_seq = 1

@router.post("", response_model=Location)
async def create_location(location: Location):
    global location_id_seq
    location.id = location_id_seq
    locations_db[location_id_seq] = location
    location_id_seq += 1
    return location

@router.get("", response_model=List[Location])
async def list_locations():
    return list(locations_db.values())

@router.get("/{location_id}", response_model=Location)
async def get_location(location_id: int):
    loc = locations_db.get(location_id)
    if not loc:
        raise HTTPException(status_code=404, detail="Location not found")
    return loc
