from pydantic import BaseModel

class HeroBase(BaseModel):
    name: str
    power: str
    age: int
    
class HeroCreate(HeroBase):
    pass  # Inherits all fields from HeroBase

class HeroResponse(HeroBase):
    id: int

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy objects
