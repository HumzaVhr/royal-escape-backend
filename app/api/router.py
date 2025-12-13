from fastapi import APIRouter
from app.modules.user.routes import router as user_router
from app.modules.pots.routes import router as pots_router


api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(pots_router)