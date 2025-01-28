

from sqlalchemy.orm import Session
from app.db.models import Battle
from  app.api.schemas  import BattleRequest

# create_battle function
def create_battle(session: Session, battle_data: BattleRequest) -> Battle:
    new_battle = Battle(**battle_data.dict())
    session.add(new_battle)
    session.commit()
    session.refresh(new_battle)
    return new_battle