import httpx

HERO_SERVICE_URL = "http://localhost:8000/heroes"

async def get_hero_by_name(hero_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{HERO_SERVICE_URL}/name/{hero_name}")
        return response.json() if response.status_code == 200 else None
