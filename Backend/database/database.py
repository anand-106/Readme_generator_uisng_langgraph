from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("DATABASE_URL")
client = AsyncIOMotorClient(MONGO_URI)
db = client['readme-ai']

user_collection=db['users']
repository_collection=db['repositories']
webhook_collection=db['webhooks']