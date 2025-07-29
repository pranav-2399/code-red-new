# mock_data.py

# --- Mock Bus Stops (10) ---
BUS_STOPS = [
    {"id": "BS1", "name": "Mylapore Tank", "lat": 13.0332, "lon": 80.2680},
    {"id": "BS2", "name": "Mandaveli", "lat": 13.0237, "lon": 80.2670},
    {"id": "BS3", "name": "Adyar Gate", "lat": 13.0102, "lon": 80.2570},
    {"id": "BS4", "name": "Saidapet", "lat": 13.0114, "lon": 80.2202},
    {"id": "BS5", "name": "Guindy", "lat": 13.0067, "lon": 80.2121},
    {"id": "BS6", "name": "Airport", "lat": 12.9903, "lon": 80.1692},
    {"id": "BS7", "name": "Tambaram", "lat": 12.9243, "lon": 80.1005},
    {"id": "BS8", "name": "Perungalathur", "lat": 12.8915, "lon": 80.0831},
    {"id": "BS9", "name": "Vandalur", "lat": 12.8922, "lon": 80.0800},
    {"id": "BS10","name": "VIT Chennai", "lat": 12.8406, "lon": 80.1536},
]

# --- Mock Bus Routes (10) ---
BUS_ROUTES = [
    {
        "id": "B100",
        "name": "Mylapore to VIT Express",
        "stops": ["BS1","BS2","BS4","BS5","BS6","BS7","BS8","BS9","BS10"],
        "frequency_min": 20,
        "distance_km": 35.5,
        "duration_min": 60
    },
    {
        "id": "B200",
        "name": "City Connector",
        "stops": ["BS1","BS3","BS4","BS5","BS6","BS7","BS10"],
        "frequency_min": 30,
        "distance_km": 32.2,
        "duration_min": 70
    }
]

# --- Mock Transit Stops (10) ---
TRANSIT_STOPS = [
    {"id": "TS1", "name": "Thirumayilai Metro", "lat": 13.0330, "lon": 80.2665},
    {"id": "TS2", "name": "Little Mount Metro", "lat": 13.0115, "lon": 80.2200},
    {"id": "TS3", "name": "Airport Metro", "lat": 12.9903, "lon": 80.1690},
    {"id": "TS4", "name": "Tambaram Station", "lat": 12.9243, "lon": 80.1002},
    {"id": "TS5", "name": "VIT Chennai Station", "lat": 12.8406, "lon": 80.1536},
]

# --- Mock Transit Routes (10) ---
TRANSIT_ROUTES = [
    {
        "id": "T100",
        "name": "Metro + Suburban Combo",
        "stops": ["TS1","TS2","TS3","TS4","TS5"],
        "frequency_min": 15,
        "distance_km": 40.0,
        "duration_min": 55
    },
    {
        "id": "T200",
        "name": "Airport Metro + Shuttle",
        "stops": ["TS1","TS3","TS5"],
        "frequency_min": 20,
        "distance_km": 38.0,
        "duration_min": 50
    }
]

