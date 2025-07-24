# wise.py

import httpx
from app.core.config import WISE_API_KEY, WISE_PROFILE_ID, WISE_API_BASE, WISE_BALANCE_ID

headers = {
    "Authorization": f"Bearer {WISE_API_KEY}",
    "Content-Type": "application/json"
}

async def get_balance():
    # Get all balances for the profile
    url = f"{WISE_API_BASE}/profiles/{WISE_PROFILE_ID}/balances/{WISE_BALANCE_ID}"
    # print(url)
    # url = f"https://api.wise.com/v4/profiles/{WISE_PROFILE_ID}/balances/{WISE_BALANCE_ID}"
    # print(url)
    # print('get_balance')
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()