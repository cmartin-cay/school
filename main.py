from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from databse.db import init_db

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/student", response_class=HTMLResponse)
async def first(request: Request):
    return templates.TemplateResponse("add_student.html", {"request": request})
