# main.py

from fastapi import FastAPI, Request 
from app.api.v1.router import router
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(title="Wise Balance Checker")
templates = Jinja2Templates(directory="app/templates")

@app.get("/dashboard", response_class=HTMLResponse)
async def show_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# Register API router
app.include_router(router, prefix="/api/v1")