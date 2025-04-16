from fastapi import APIRouter, HTTPException
from models import User
from typing import List
from bson import ObjectId
from bson.errors import InvalidId

router = APIRouter()

async def get_users_collection():
    from db import init_db
    return init_db()["users_collection"]

# Fix
@router.get("/", response_model=List[User])
async def get_users():
    collection = await get_users_collection()
    users = []
    async for user in collection.find():
        # Only include fields defined in User model
        users.append({"username": user["username"], "bio": user["bio"]})
    return users

# Fix
@router.post("/", status_code=201)
async def create_user(user: User):
    collection = await get_users_collection()
    if await collection.find_one({"username": user.username}):
        raise HTTPException(400, "Username already exists")  #Check duplicates
    result = await collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}

# Fix
@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: str):
    try:
        collection = await get_users_collection()
        result = await collection.delete_one({"_id": ObjectId(user_id)})
    except InvalidId:
        raise HTTPException(400, "Invalid user ID format")  # Handle malformed IDs
    if not result.deleted_count:
        raise HTTPException(404, "User not found")