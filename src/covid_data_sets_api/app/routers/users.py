from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_sqlalchemy import db
from sqlalchemy.sql.expression import delete
from typing import Union, List
from uuid import UUID, uuid4
from jose import jwt, JWTError
from schema import ApiUser as SchemaApiUser
from schema import GenericResponse as SchemaGenericResponse
from schema import ApiUser, GenericResponse
from models import ApiUser as ModelApiUser
from utils import auth

router = APIRouter()

CUSTOM_AUTH = auth.CustomAuth()

#user authentication

async def get_user_to_authenticate(username: str) -> ModelApiUser:
    result = await db.session.query(ModelApiUser).filter(ModelApiUser.username == username)
    return result

async def authenticate_user(username: str, password: str):
    user = await get_user_to_authenticate(username)
    if not user:
        return False
    if not CUSTOM_AUTH._verify_password(password, user.password):
        return False
    return user  

async def get_current_user(token):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = {"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, CUSTOM_AUTH._SECRET_KEY, algorithms=[CUSTOM_AUTH._ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = auth.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await db.session.query(ModelApiUser).filter(ModelApiUser.username == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user           

    
# async def get_current_active_user(current_user: ModelApiUser = Depends(get_current_user)):
#     if current_user.





@router.get(
    "/get_all_users", 
    response_model= List[SchemaApiUser],
    tags=["users"]
)
async def get_all_user():
    return db.session.query(ModelApiUser).all()



