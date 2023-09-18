from fastapi import FastAPI
from db import init_db

app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init_db()