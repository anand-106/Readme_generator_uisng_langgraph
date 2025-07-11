from .database import user_collection,repository_collection,webhook_collection
import uuid
import secrets
from api.utils.github_api import disable_webhook_github,delete_webhook_github
from api.utils.github_utils import clean_mongo_doc


async def register_user_db(user_data:dict,repo_data:dict):
    
    try:
        
        existing_user = await user_collection.find_one({"username":user_data["username"]})
        
        
        
        if existing_user:
            print("User already exists in db")
            result = await user_collection.update_one(
                                                        {"username": user_data["username"]},
                                                        {"$set": {"github_token": user_data["github_token"]}}
                                                    )
            await repository_collection.delete_many({"user_id": user_data["user_id"]})
            print("Old repos deleted")
            
            if repo_data:
                await repository_collection.insert_many(repo_data)
                print("New repos inserted")
            
            print("token updated")
            return "user exists and updated"
        
        if repo_data:
                await repository_collection.insert_many(repo_data)
        
        await user_collection.insert_one(user_data)
        
        
        
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
            
        user_data = clean_mongo_doc(dict(user))
        return user_data
        
    except Exception as e:
         print(f'error getting token from db : {e}')
         return

async def set_webhook_db(user_id:str,repo_id:str,hook_url:str,hook_id,secret,):
    
    try:
        webhook_data = {
                "user_id":user_id,
                "repo_id":repo_id,
                "webhook_id":str(uuid.uuid4()),
                "secret":secret,
                "webhook_url":"https://30b8-106-219-160-120.ngrok-free.app/api/github/generate",
                "hook_url":hook_url,
                "hook_id":hook_id,
                "isActive":True
            }
        await webhook_collection.insert_one(
            webhook_data
        )
        print("webhook created succesfully")
        return webhook_data
    except Exception as e:
        print(f'error creating webhook {e}')

async def get_webhook_data_db(repo_id:str):
    
    try:
        webhook =  await webhook_collection.find_one({"repo_id":repo_id})
        
        if not webhook:
            print("Webhook not found on db")
            return
        webhook_data = clean_mongo_doc(dict(webhook))
        
        return webhook_data
        
    except Exception as e:
        print(f'error getting webhook {e}')

async def set_status_webhook_be(repo_id:str,access_token:str,isActive:bool):
    try:
        webhook =  await webhook_collection.update_one({"repo_id":repo_id},{'$set':{"isActive":isActive}})
        print("webhook disabled on db")
        
        webhook_data = await get_webhook_data_db(repo_id)
        
        await disable_webhook_github(hook_url=webhook_data["hook_url"],access_token=access_token,isActive=isActive)
        print("webhook disabled on github")  
        
    except Exception as e:
        print(f'error disabling webhook {e}')

async def delete_webhook_be(repo_id:str,access_token:str):
    try:
        webhook_data = await get_webhook_data_db(repo_id)
        
        webhook = await webhook_collection.delete_one({"repo_id":repo_id})
        print("webhook deleted on db")
        
        
        
        await delete_webhook_github(hook_url=webhook_data["hook_url"],access_token=access_token)
        print("webhook deleted on github")
        
        
    except Exception as e:
        print(f'error deleting webhook {e}')


async def get_repos_by_ids(repo_ids: list[str]):
    cursor = repository_collection.find({"repo_id": {"$in": repo_ids}})
    repos = await cursor.to_list(length=None)
    return [clean_mongo_doc(r) for r in repos]

        
async def get_webhook_repos(user_id:str):
    
    cursor = webhook_collection.find({"user_id":user_id})
    
    raw_webhooks = await cursor.to_list(length=None)

    cleaned_webhooks = [clean_mongo_doc(r) for r in raw_webhooks]
    
    repo_ids = [w["repo_id"] for w in cleaned_webhooks]
    
    repos = await get_repos_by_ids(repo_ids)
    
    return repos
    



        

