"""
Service layer for shipment operations.
"""
import requests
from typing import List
from datetime import datetime
from app.models.shipment import Shipment, Location
from config import settings

class ShipmentService:
    @staticmethod
    def calculate_route(origin: Location, destination: Location) -> List[Location]:
        """Call Google Maps Directions API to get optimal route.
        Returns a list of Location points along the route.
        """
        url = "https://maps.googleapis.com/maps/api/directions/json"
        params = {
            "origin": f"{origin.latitude},{origin.longitude}",
            "destination": f"{destination.latitude},{destination.longitude}",
            "key": settings.GOOGLE_MAPS_API_KEY,
            "mode": "driving",
            "alternatives": "false",
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if data["status"] != "OK":
            raise ValueError(f"Google Maps API error: {data['status']} - {data.get('error_message')}"
)
        # Extract polyline points
        route_points = []
        for leg in data["routes"][0]["legs"]:
            for step in leg["steps"]:
                start_loc = step["start_location"]
                route_points.append(
                    Location(
                        latitude=start_loc["lat"],
                        longitude=start_loc["lng"],
                        timestamp=datetime.utcnow(),
                    )
                )
        return route_points

    @staticmethod
    def estimate_cost(route: List[Location]) -> float:
        """Simple cost estimation: $0.5 per km.
        For demo purposes, we calculate straight-line distance.
        """
        if not route:
            return 0.0
        # Haversine formula
        from math import radians, cos, sin, asin, sqrt

        def haversine(lat1, lon1, lat2, lon2):
            R = 6371  # Earth radius in km
            dlat = radians(lat2 - lat1)
            dlon = radians(lon2 - lon1)
            a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
            c = 2 * asin(sqrt(a))
            return R * c

        total_distance = 0.0
        for i in range(1, len(route)):
            total_distance += haversine(
                route[i - 1].latitude,
                route[i - 1].longitude,
                route[i].latitude,
                route[i].longitude,
            )
        return round(total_distance * 0.5, 2)

    @staticmethod
    def create_shipment(shipment_data: Shipment) -> Shipment:
        """Create a shipment, calculate route and cost.
        In a real system, this would persist to DB.
        """
        route = ShipmentService.calculate_route(shipment_data.origin, shipment_data.destination)
        cost = ShipmentService.estimate_cost(route)
        shipment_data.route = route
        shipment_data.estimated_cost = cost
        shipment_data.status = "scheduled"
        shipment_data.updated_at = datetime.utcnow()
        # TODO: Persist to database
        return shipment_data
