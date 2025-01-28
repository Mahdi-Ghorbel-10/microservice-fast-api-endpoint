from sqlalchemy.orm import Session
from app.db.models import Hero
from app.api.schemas import HeroCreate

# Create a new hero
def create_hero(session: Session, hero_data: HeroCreate) -> Hero:
    new_hero = Hero(**hero_data.dict())  # Convert Pydantic model to dict
    session.add(new_hero)
    session.commit()
    session.refresh(new_hero)  # Refresh to fetch the generated ID
    return new_hero

# Get all heroes with optional pagination
def get_heroes(session: Session, skip: int = 0, limit: int = 10) -> list[Hero]:
    return session.query(Hero).offset(skip).limit(limit).all()

# Get a single hero by ID
def get_hero_by_id(session: Session, hero_id: int) -> Hero | None:
    return session.query(Hero).filter(Hero.id == hero_id).first()

# Update a hero
def update_hero(session: Session, hero_id: int, hero_data: HeroCreate) -> Hero | None:
    hero = session.query(Hero).filter(Hero.id == hero_id).first()
    if hero:
        for key, value in hero_data.dict().items():
            setattr(hero, key, value)  # Update fields dynamically
        session.commit()
        session.refresh(hero)
    return hero

# Delete a hero
def delete_hero(session: Session, hero_id: int) -> bool:
    hero = session.query(Hero).filter(Hero.id == hero_id).first()
    if hero:
        session.delete(hero)
        session.commit()
        return True
    return False
