from pydantic import BaseModel

class BattleRequest(BaseModel):
    hero_name: str
    villain_name: str

class BattleResult(BaseModel):
    hero: str
    villain: str
    winner: str
    reason: str
