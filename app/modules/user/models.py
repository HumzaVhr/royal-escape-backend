from pydantic import BaseModel, Field
from bson import ObjectId


class User(BaseModel):
    id: ObjectId | None = Field(default=None, alias="_id")
    phone: str
    is_verified: bool = False


    class Config:
        arbitrary_types_allowed = True