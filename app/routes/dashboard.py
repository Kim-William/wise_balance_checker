from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.services.wise import get_balance

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/dashboard", response_class=HTMLResponse)
async def show_dashboard(request: Request):
    balances = await get_balance()

    # EUR 기준 첫 번째 잔액만 사용 (필요 시 조건 분기)
    eur_balance = next((b for b in balances if b['currency'] == 'EUR'), None)
    amount = eur_balance['amount']['value'] if eur_balance else 'N/A'

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "balance": amount,
        "currency": eur_balance['currency'] if eur_balance else 'EUR',
        "user_role": "family"  # 임시 하드코딩
    })