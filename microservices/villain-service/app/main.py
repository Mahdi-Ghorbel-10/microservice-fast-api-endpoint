from fastapi import FastAPI
from app.api.routers import villain_router

app = FastAPI(title="Villain API")
app.include_router(villain_router, prefix="/villains")
