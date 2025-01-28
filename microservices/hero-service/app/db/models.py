from sqlalchemy import Column, Integer, String, Boolean
from app.db.base   import Base



class Hero(Base):
    __tablename__ = "microservice_heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    power = Column(String)
    age = Column(Integer)