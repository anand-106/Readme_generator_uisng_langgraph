from jose import JWTError, jwt
import os
from dotenv import load_dotenv
from fastapi import HTTPException,status


def create_jwt_token(data:dict):
    
    load_dotenv()
    
    token = os.getenv("JWT_SECRET")
    return jwt.encode(data,token)

def verify_jwt_token(token:str):
    try:
        secret = os.getenv("JWT_SECRET")
        payload = jwt.decode(token,secret)
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    