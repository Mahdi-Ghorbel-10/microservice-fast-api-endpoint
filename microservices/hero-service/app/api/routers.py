from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.crud import (
    create_hero,
    get_heroes,
    get_hero_by_id,
    get_hero_by_name,
    update_hero,
    delete_hero,
)
from app.api.schemas import HeroCreate, HeroResponse
from app.db.session import SessionLocal

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

# Create a new hero
@router.post("/", response_model=HeroResponse)
def create_hero_endpoint(hero: HeroCreate, db: Session = Depends(get_db)):
    return create_hero(db, hero)

# Get all heroes
@router.get("/", response_model=list[HeroResponse])
def get_heroes_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_heroes(db, skip=skip, limit=limit)

# Get a single hero by ID
@router.get("/{hero_id}", response_model=HeroResponse)
def get_hero_endpoint(hero_id: int, db: Session = Depends(get_db)):
    hero = get_hero_by_id(db, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

# GET a hero by name 
@router.get("/name/{hero_name}", response_model=HeroResponse)
def get_hero_by_name_endpoint(hero_name: str, db: Session = Depends(get_db)):
    hero = get_hero_by_name(db, hero_name)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

# Update a hero
@router.put("/{hero_id}", response_model=HeroResponse)
def update_hero_endpoint(hero_id: int, hero: HeroCreate, db: Session = Depends(get_db)):
    updated_hero = update_hero(db, hero_id, hero)
    if not updated_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return updated_hero

# Delete a hero
@router.delete("/{hero_id}", response_model=dict)
def delete_hero_endpoint(hero_id: int, db: Session = Depends(get_db)):
    success = delete_hero(db, hero_id)
    if not success:
        raise HTTPException(status_code=404, detail="Hero not found")
    return {"message": "Hero deleted successfully"}
