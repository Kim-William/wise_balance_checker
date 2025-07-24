# routes.py

from fastapi import APIRouter
from app.services.wise import get_balance

router = APIRouter()

@router.get("/bal")
async def read_balance():
    print('asdaaaa')
    # Fetch and return Wise balance data
    return await get_balance()