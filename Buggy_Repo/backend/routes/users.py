from fastapi import APIRouter, HTTPException
from models import User
from bson import ObjectId
from bson.errors import InvalidId

router = APIRouter()

async def get_users_collection():
    from db import init_db
    return init_db()["users_collection"]

@router.get("/")
async def get_users():
    collection = await get_users_collection()
    users = []
    async for user in collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users

# Fix
@router.post("/", status_code=201)
async def create_user(user: User):
    collection = await get_users_collection()
    if await collection.find_one({"username": user.username}):
        raise HTTPException(400, "Username already exists")  #Check duplicates
    result = await collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}

@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: str):
    try:
        collection = await get_users_collection()
        result = await collection.delete_one({"_id": ObjectId(user_id)})
    except InvalidId:
        raise HTTPException(400, "Invalid user ID format")  # Handle malformed IDs
    if not result.deleted_count:
        raise HTTPException(404, "User not found")