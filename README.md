# Pheidippides  
*The first person to run a marathon, now powering the most efficient routing solution.*

---

## Overview
**Pheidippides** is a unique route optimization solution that takes **source** and **destination** locations as input and determines:  
- The **best and shortest route** between the two points.  
- The **cheapest route** by integrating public transport hubs (metro stations, bus stops, transit routes).  
- The estimated **Uber cost** (bike & car options) for the same route.  
- **Sightseeing spots** along the route, adjusting the recommendation accordingly.

Unlike any existing solution, **Pheidippides uses real-time transit data** to recommend the **most efficient route** in real-world conditions.  
> **Unique Selling Proposition (USP):**  
> There is no existing product in the market offering this combination of **real-time transit integration, cost estimation, and sightseeing-aware routing**.  
> The complexity and uniqueness of this system make it difficult to replicate or mock using any AI agent or LLM model.

---

## Features
1. **Best & Shortest Route**  
   - Uses advanced routing algorithms to compute optimal paths based on real-time traffic data.

2. **Cheapest Route (Transit-Aware)**  
   - Identifies nearby transport hubs (e.g., metro stations, bus terminals).  
   - Suggests routes minimizing cost through an intelligent mix of walking, transit, and cab rides.

3. **Cost Estimation via Uber**  
   - Calls Uber API endpoints to fetch approximate trip costs for:  
     - **Bike** (low cost)  
     - **Car** (standard ride)  
   - Provides per-person cost estimates.

4. **Sightseeing Recommendations**  
   - Scans the route for popular sightseeing spots.  
   - Suggests scenic alternative routes for enhanced travel experience.

5. **USP Highlight**  
   - **Real-Time Transit Data Integration**: Not just static map routes.  
   - **Multi-Modal Routing**: Combines public transport and ride-hailing dynamically.  
   - **AI-Resistant Approach**: A first-of-its-kind system built on live data, not just predictive models.

---

## Tech Stack
- **Backend Framework:** FastAPI (Python)  
- **Map & Routing Data:** OpenStreetMap / OpenRouteService  
- **Transit Data:** GTFS or city-specific transit APIs  
- **Cost Estimation:** Uber API endpoints  
- **Data Processing:** Python (GeoJSON handling, distance calculation, cost aggregation)

---

## Input & Output
### Input
- **Source Location:** Latitude & Longitude or place name  
- **Destination Location:** Latitude & Longitude or place name  

### Output
- Shortest route visualization  
- Cheapest route (with transit hubs)  
- Uber cost estimation (bike/car)  
- Optional sightseeing-based alternate route  

---

## Example Flow
1. **User Inputs**  
   - Source: `Mylapore, Chennai`  
   - Destination: `VIT Chennai`

2. **System Processes**  
   - Finds shortest route via roads  
   - Identifies nearest transit hubs (e.g., metro station, bus route)  
   - Fetches Uber ride cost  
   - Searches for sightseeing along the way  

3. **Output Example**
   - **Shortest Route:** 35 mins via Mount Road  
   - **Cheapest Route:** Walk to Mylapore Metro → Metro to Guindy → Bus to VIT Chennai (₹40)  
   - **Uber (Car):** ₹350 (est.) | **Uber (Bike):** ₹150 (est.)  
   - **Sightseeing Suggestion:** Marina Beach (adds 10 mins)

---

## Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/pheidippides.git
   cd pheidippides
