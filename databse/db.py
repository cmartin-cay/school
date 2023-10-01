from beanie import init_beanie
import motor.motor_asyncio
import os
from models.people_model import Student, Teacher
from dotenv import load_dotenv


load_dotenv()
DB_NAME = os.environ.get("DB_NAME")
DB_PASS = os.environ.get("DB_PASS")
uri = f"mongodb+srv://{DB_NAME}:{DB_PASS}@cluster0.q0dozh3.mongodb.net/?retryWrites=true&w=majority"

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    await init_beanie(database=client.school, document_models=[Student, Teacher])
