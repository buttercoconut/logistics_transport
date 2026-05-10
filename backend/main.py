"""
FastAPI application entry point.
"""
from fastapi import FastAPI
from app.api.shipments import router as shipments_router

app = FastAPI(title="Logistics Transport API", version="1.0.0")

# Include routers
app.include_router(shipments_router, prefix="/api/shipments", tags=["shipments"])

# Health check endpoint
@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}
