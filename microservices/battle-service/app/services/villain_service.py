import httpx

VILLAIN_SERVICE_URL = "http://localhost:8001/villains"

async def get_villain_by_name(villain_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{VILLAIN_SERVICE_URL}/name/{villain_name}")
        return response.json() if response.status_code == 200 else None
