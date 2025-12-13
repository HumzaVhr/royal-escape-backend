from datetime import datetime
from bson import ObjectId
from app.core.database import db

from app.core.security import create_access_token


async def verify_otp_and_login(user_id: str):
    return create_access_token(subject=user_id)


async def create_user(data: dict):
    now = datetime.utcnow()
    user = {
    **data,
    "is_verified": True,
    "created_at": now,
    "updated_at": now,
    }
    result = await db.users.insert_one(user)
    await db.user_wallets.insert_one({
    "user_id": result.inserted_id,
    "balance": 0,
    "currency": "INR",
    "updated_at": now
    })
    return result.inserted_id


async def get_user(user_id: str):
    return await db.users.find_one({"_id": ObjectId(user_id)})


async def get_dashboard(user_id: str):
    wallet = await db.user_wallets.find_one({"user_id": ObjectId(user_id)})
    entries = await db.user_entries.count_documents({"user_id": ObjectId(user_id)})
    winnings = await db.user_winnings.aggregate([
    {"$match": {"user_id": ObjectId(user_id)}},
    {"$group": {"_id": None, "total": {"$sum": "$amount"}}}
    ]).to_list(1)


    return {
    "balance": wallet["balance"],
    "total_entries": entries,
    "total_winnings": winnings[0]["total"] if winnings else 0
    }