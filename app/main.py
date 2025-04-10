from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.db.tables_queries import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create tables in the database on startup"""
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}