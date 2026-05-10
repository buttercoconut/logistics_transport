# main.py
from fastapi import FastAPI
from .api import shipments, carriers, drivers, locations

app = FastAPI(title="Logistics Transport API", version="1.0.0")

app.include_router(shipments.router)
app.include_router(carriers.router)
app.include_router(drivers.router)
app.include_router(locations.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
