from .database import user_collection,repository_collection,webhook_collection
import uuid
import secrets


async def register_user_db(user_data:dict,repo_data:dict):
    
    try:
        
        existing_user = await user_collection.find_one({"username":user_data["username"]})
        
        if existing_user:
            print("User already exists in db")
            result = await user_collection.update_one(
                                                        {"username": user_data["username"]},
                                                        {"$set": {"github_token": user_data["github_token"]}}
                                                    )
            print("token updated")
            return "user exists"
        
        
        await user_collection.insert_one(user_data)
        
        if repo_data:
            await repository_collection.insert_many(repo_data)
        
        print("user and repo data inserted")
        return "Inserted"
    except Exception as e:
        print(f'error updating db: {e}')
        return "Error"   
    
async def get_github_user_data(username:str):
    
    try:
        user = await user_collection.find_one({"username":username})
        
        if not user:
            print("user not found in db")
            return
            
        user_data = dict(user)
        return user_data
        
    except Exception as e:
         print(f'error getting token from db : {e}')
         return

async def set_webhook_db(user_id:str,repo_id:str):
    
    try:
        webhook_data = {
                "user_id":user_id,
                "repo_id":repo_id,
                "webhook_id":str(uuid.uuid4()),
                "secret":secrets.token_hex(32),
                "webhook_url":"https://30b8-106-219-160-120.ngrok-free.app/api/github/generate"
            }
        await webhook_collection.insert_one(
            webhook_data
        )
        print("webhook created succesfully")
        return webhook_data
    except Exception as e:
        print(f'error creating webhook {e}')