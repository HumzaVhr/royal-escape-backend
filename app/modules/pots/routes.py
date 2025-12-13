from fastapi import APIRouter, Depends
from app.core.database import db


router = APIRouter(prefix="/pots", tags=["pots"])


@router.post("/")
async def create_pot(pot: dict):
    await db.pots.insert_one(pot)
    return pot


@router.get("/")
async def list_pots():
    return await db.pots.find().to_list(100)