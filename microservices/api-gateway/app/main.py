from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI(title="API Gateway")

# Microservice URLs
HERO_SERVICE_URL = "http://localhost:8000"
VILLAIN_SERVICE_URL = "http://localhost:8001"
BATTLE_SERVICE_URL = "http://localhost:8002"

@app.get("/heroes/name/{hero_name}")
async def route_to_hero_service(hero_name: str):
    """Route to Hero Service"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{HERO_SERVICE_URL}/heroes/name/{hero_name}")
        return response.json()

@app.get("/villains")
async def route_to_villain_service(villain_name: str):
    """Route to Villain Service"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{VILLAIN_SERVICE_URL}/villains")
        return response.json()

@app.post("/battles/battle")
async def route_to_battle_service(data: dict):
    """Route to Battle Service"""
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BATTLE_SERVICE_URL}/battles/battle", json=data)
        return response.json()
