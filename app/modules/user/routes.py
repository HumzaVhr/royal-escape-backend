from fastapi import APIRouter
from app.modules.user.schemas import UserCreateSchema
from app.modules.user.service import create_user, get_user, get_dashboard
from fastapi import APIRouter, Depends
from app.api.deps import get_current_user


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
async def register_user(payload: UserCreateSchema):
    user_id = await create_user(payload.model_dump())
    return {"user_id": str(user_id)}


@router.get("/{user_id}")
async def fetch_user(user_id: str):
    return await get_user(user_id)


@router.get("/{user_id}/dashboard")
async def user_dashboard(user_id: str):
    return await get_dashboard(user_id)


@router.get("/me")
async def my_profile(current_user=Depends(get_current_user)):
    return current_user


@router.get("/me/dashboard")
async def my_dashboard(current_user=Depends(get_current_user)):
    from app.modules.user.service import get_dashboard
    return await get_dashboard(str(current_user["_id"]))