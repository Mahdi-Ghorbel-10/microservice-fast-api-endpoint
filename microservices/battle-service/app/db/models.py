from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base
from app.db.session import Session
from app.api.schemas import BattleRequest
class Battle(Base):
    __tablename__ = "battles"

    id = Column(Integer, primary_key=True, index=True)
    hero_name = Column(String, index=True)
    villain_name = Column(String, index=True)
    winner = Column(String, index=True)


#create a battle
def create_battle(session: Session, battle_data: BattleRequest) -> Battle:
    new_battle = Battle(**battle_data.dict())
    session.add(new_battle)
    session.commit()
    session.refresh(new_battle)
    return new_battle