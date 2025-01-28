from fastapi import APIRouter, HTTPException
from app.services.hero_service import get_hero_by_name
from app.services.villain_service import get_villain_by_name
from app.services.logic import determine_winner
from app.api.schemas import BattleRequest, BattleResult
import asyncio

router = APIRouter()

@router.post("/battle", response_model=BattleResult)
async def battle(request: BattleRequest):
    """User selects a hero and villain for battle."""
    
    hero = await get_hero_by_name(request.hero_name)
    villain = await get_villain_by_name(request.villain_name)

    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    if not villain:
        raise HTTPException(status_code=404, detail="Villain not found")

    winner, reason = determine_winner(hero, villain)

    return {"hero": hero["name"], "villain": villain["name"], "winner": winner, "reason": reason}
