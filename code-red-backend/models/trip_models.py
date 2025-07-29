from pydantic import BaseModel

class Coordinate(BaseModel):
    latitude: float
    longitude: float

class TripRequest(BaseModel):
    source: Coordinate
    destination: Coordinate

class TripResponse(BaseModel):
    route: list
