from fastapi import FastAPI
from .db import connect_db, close_db
from .routers import health

app = FastAPI(title="GreenSnap API")

@app.get("/")
def root():
    return {"message": "GreenSnap API is running"}

app.include_router(health.router)

@app.on_event("startup")
async def startup():
    await connect_db()

@app.on_event("shutdown")
async def shutdown():
    await close_db()
