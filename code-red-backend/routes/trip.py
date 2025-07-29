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

    response.raise_for_status()  # raises an HTTPError for bad responses
    data = response.json()

    if "features" not in data:
        raise ValueError("Missing 'features' in ORS response")

    geometry = data["features"][0]["geometry"]
    return geometry["coordinates"]
