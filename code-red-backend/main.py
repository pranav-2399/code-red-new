from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated
from services.ors import get_route
from mock_data import BUS_STOPS, BUS_ROUTES, TRANSIT_STOPS, TRANSIT_ROUTES
import os
import json
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Trip Planner API!",
        "usage": "POST to /trip/plan with source and destination coordinates."
    }


class Coordinate(BaseModel):
    latitude: Annotated[float, Field(..., ge=-90, le=90)]
    longitude: Annotated[float, Field(..., ge=-180, le=180)]


class TripRequest(BaseModel):
    source: Coordinate
    destination: Coordinate


@app.post("/trip/plan")
async def plan_trip(data: TripRequest):
    try:
        route_info = await get_route(
            {"latitude": data.source.latitude, "longitude": data.source.longitude},
            {"latitude": data.destination.latitude, "longitude": data.destination.longitude}
        )
        return {
            "status": "success",
            "route": route_info
        }
    except Exception as e:
        print(f"🔥 Internal error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/bus/stops")
def get_bus_stops():
    return {"bus_stops": BUS_STOPS}

@app.get("/bus/routes")
def get_bus_routes():
    return {"bus_routes": BUS_ROUTES}

@app.get("/transit/stops")
def get_transit_stops():
    return {"transit_stops": TRANSIT_STOPS}

@app.get("/transit/routes")
def get_transit_routes():
    return {"transit_routes": TRANSIT_ROUTES}

class RouteData(BaseModel):
    source: dict
    destination: dict
    timestamp: str

from services.generate import run_gemini_generation

@app.post("/transit/locations")
async def receive_route(data: RouteData):
    print("✅ Received route:", data)

    save_dir = "saved_routes"
    os.makedirs(save_dir, exist_ok=True)

    route_path = os.path.join(save_dir, "route_temp.json")
    
    # Save the incoming data
    with open(route_path, "w") as f:
        json.dump(data.dict(), f, indent=2)

    try:
        # Run Gemini generation
        output_text = run_gemini_generation(
            route_json_path=route_path
        )

        # ✅ After successful generation, remove the file
        if os.path.exists(route_path):
            os.remove(route_path)
            print("🧹 Temporary route file deleted.")

        return {
            "status": "success",
            "message": output_text
        }

    except Exception as e:
        print("🔥 Gemini generation failed:", e)

        # ❗ Optional: Still remove file if it exists, even on error
        if os.path.exists(route_path):
            os.remove(route_path)
            print("🧹 Cleaned up temp file after error.")

        return {
            "status": "error",
            "message": "Gemini failed: " + str(e)
        }