from pydantic import BaseModel

class VillainBase(BaseModel):
    name: str
    power: str
    age: int

class VillainCreate(VillainBase):
    pass  # Inherits all fields from VillainBase

class VillainResponse(VillainBase):
    id: int

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy objects