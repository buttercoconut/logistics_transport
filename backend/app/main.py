# main.py
from fastapi import FastAPI
from .api import shipments, carriers, drivers, locations

app = FastAPI(title="Logistics Transport API")

app.include_router(shipments.router, prefix="/shipments", tags=["shipments"])
app.include_router(carriers.router, prefix="/carriers", tags=["carriers"])
app.include_router(drivers.router, prefix="/drivers", tags=["drivers"])
app.include_router(locations.router, prefix="/locations", tags=["locations"])

@app.get("/")
async def root():
    return {"message": "Welcome to Logistics Transport API"}
