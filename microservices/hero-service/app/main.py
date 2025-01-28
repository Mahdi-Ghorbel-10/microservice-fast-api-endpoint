from fastapi import FastAPI
from app.api.routers import router as hero_router

app = FastAPI(title="Hero API")
app.include_router(hero_router, prefix="/heroes")

@app.get("/")
def root():
    return {"message": "Welcome to the Hero API!"}
