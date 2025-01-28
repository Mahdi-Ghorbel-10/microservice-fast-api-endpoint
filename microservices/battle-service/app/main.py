from fastapi import FastAPI
from app.api.routers import router as battle_router
from app.db.base import Base
from app.db.session import engine

# Initialize the database tables
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI(title="Battle Service", description="Manage battles between heroes and villains", version="1.0")

# Include the battle API router
app.include_router(battle_router, prefix="/battles", tags=["Battles"])

@app.get("/")
async def root():
    return {"message": "Battle Service is running!"}
