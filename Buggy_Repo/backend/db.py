from motor.motor_asyncio import AsyncIOMotorClient
import os

def init_db():
    MONGO_URI = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["testdb"]
    # BUG (old code): quiz_collection not returned
    # CHANGES: Added quiz_collection to the returned dictionary
    return {
        "items_collection": db["item"],
        "users_collection": db["users"],
        "quiz_collection": db["quiz"]
    }
    # Question for chocolate: How can we implement nosql syntax in mysql ???