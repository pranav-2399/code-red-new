import os
import httpx
from dotenv import load_dotenv

load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY")
ORS_BASE_URL = "https://api.openrouteservice.org/v2/directions/driving-car"

async def get_route(source: dict, destination: dict):
    headers = {
        "Authorization": ORS_API_KEY,
        "Content-Type": "application/json"
    }
    body = {
        "coordinates": [
            [source["longitude"], source["latitude"]],
            [destination["longitude"], destination["latitude"]]
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(ORS_BASE_URL, headers=headers, json=body)

    response.raise_for_status()
    data = response.json()

    # 🔄 Adapted for "routes" response
    if "routes" not in data or not data["routes"]:
        raise ValueError("Missing 'routes' in ORS response")

    route = data["routes"][0]
    segment = route["segments"][0]

    return {
        "distance_km": round(segment["distance"] / 1000, 2),
        "duration_min": round(segment["duration"] / 60, 2),
        "route_geometry": route["geometry"]  # Encoded polyline
    }
