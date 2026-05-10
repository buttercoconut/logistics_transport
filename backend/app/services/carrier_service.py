# services/carrier_service.py
from typing import List
from ..models.carrier import Carrier, CarrierCreate

# In-memory store for demo
carriers_db = {}
carrier_id_seq = 1

async def create_carrier(carrier_in: CarrierCreate) -> Carrier:
    global carrier_id_seq
    carrier = Carrier(id=carrier_id_seq, name=carrier_in.name, rating=carrier_in.rating, drivers=[])
    carriers_db[carrier_id_seq] = carrier
    carrier_id_seq += 1
    return carrier

async def get_carrier(carrier_id: int) -> Carrier:
    return carriers_db.get(carrier_id)

async def list_carriers() -> List[Carrier]:
    return list(carriers_db.values())
