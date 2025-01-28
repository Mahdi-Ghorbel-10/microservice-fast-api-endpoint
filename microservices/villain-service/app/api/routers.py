from fastapi import APIRouter, HTTPException
from app.crud.crud import get_all_villains, add_villain, get_villain_by_name, delete_villain
from app.db.models import Villain

villain_router = APIRouter()

@villain_router.get("/")
async def list_villains():
    return get_all_villains()

@villain_router.post("/")
async def create_villain(villain: Villain):
    add_villain(villain)
    return {"message": "Villain added", "villain": villain}

@villain_router.get("/{name}")
async def read_villain(name: str):
    villain = get_villain_by_name(name)
    if not villain:
        raise HTTPException(status_code=404, detail="Villain not found")
    return villain

@villain_router.delete("/{name}")
async def remove_villain(name: str):
    result = delete_villain(name)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Villain not found")
    return {"message": f"Villain {name} deleted"}
