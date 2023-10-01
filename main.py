from fastapi import FastAPI

from databse.db import init_db

app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/first")
async def first():
    return{"message": "first route"}