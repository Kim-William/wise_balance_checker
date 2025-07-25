# main.py

from fastapi import FastAPI, Request 
from app.api.v1.router import router
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.services.wise import get_balance

app = FastAPI(title="Wise Balance Checker")
templates = Jinja2Templates(directory="app/templates")

@app.get("/dashboard", response_class=HTMLResponse)
async def show_dashboard(request: Request):
    balance_data = await get_balance()
    
    # 확인된 구조 기준
    amount = balance_data['amount']['value']
    currency = balance_data['currency']

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "balance": amount,
        "currency": currency,
        "user_role": "family"
    })

# Register API router
app.include_router(router, prefix="/api/v1")