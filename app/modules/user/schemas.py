from pydantic import BaseModel, EmailStr
from typing import Optional


class SendOTPRequest(BaseModel):
    phone: str


class VerifyOTPRequest(BaseModel):
    phone: str
    otp: str


class AddressSchema(BaseModel):
    line1: str
    city: str
    state: str
    pincode: str


class UserCreateSchema(BaseModel):
    phone: str
    email: Optional[EmailStr]
    name: str
    address: AddressSchema


class UserResponseSchema(UserCreateSchema):
    id: str


class DashboardSchema(BaseModel):
    balance: float
    total_entries: int
    total_winnings: float