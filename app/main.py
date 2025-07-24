# main.py

from fastapi import FastAPI
from app.api.v1.router import router

app = FastAPI(
    title="Wise Balance Checker"
)

# Register API router
print('asdasd')
app.include_router(router, prefix="/api/v1")