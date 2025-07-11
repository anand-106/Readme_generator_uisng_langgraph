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



from api.utils.github_utils import clean_mongo_doc

async def get_repos(user_id: str):
    try:
        cursor = repository_collection.find({"user_id": user_id})
        raw_repos = await cursor.to_list(length=None)

        cleaned_repos = [clean_mongo_doc(r) for r in raw_repos]

        print("retrieved repos from db")

        return cleaned_repos
    except Exception as e:
        print(f"error getting webhook repos {e}")
