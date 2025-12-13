from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import decode_access_token
from app.core.database import db
from bson import ObjectId


security = HTTPBearer()


async def get_current_user(
credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials
    user_id = decode_access_token(token)


    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user