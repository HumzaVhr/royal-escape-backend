from app.core.database import db
from app.utils.otp import send_otp
from app.core.security import create_access_token


async def request_otp(phone: str):
    await send_otp(phone)


async def verify_otp(phone: str, otp: str):
    # OTP validation mocked
    user = await db.users.find_one({"phone": phone})
    if not user:
        await db.users.insert_one({"phone": phone, "is_verified": True})
    token = create_access_token({"sub": phone})
    return token