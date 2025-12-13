from fastapi import APIRouter
from app.modules.user.schemas import SendOTPRequest, VerifyOTPRequest
from app.modules.user.service import request_otp, verify_otp


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/otp")
async def send_otp(req: SendOTPRequest):
    await request_otp(req.phone)
    return {"message": "OTP sent"}


@router.post("/verify")
async def verify(req: VerifyOTPRequest):
    token = await verify_otp(req.phone, req.otp)
    return {"access_token": token, "token_type": "bearer"}