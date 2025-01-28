from pydantic import BaseModel

class Villain(BaseModel):
    name: str
    evil_power: str
    is_evil: bool = True
