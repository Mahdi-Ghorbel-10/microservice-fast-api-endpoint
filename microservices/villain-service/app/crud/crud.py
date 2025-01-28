from app.db.session import villain_collection
from app.db.models import Villain

def get_all_villains():
    return list(villain_collection.find({}, {"_id": 0}))  # Exclude `_id` field

def add_villain(villain: Villain):
    villain_collection.insert_one(villain.dict())

def get_villain_by_name(name: str):
    return villain_collection.find_one({"name": name}, {"_id": 0})

def delete_villain(name: str):
    return villain_collection.delete_one({"name": name})
