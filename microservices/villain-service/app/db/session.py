from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"
client = MongoClient(MONGO_URL)

# Define the database
db = client["villain_db"]

# Define collections
villain_collection = db["villains"]
