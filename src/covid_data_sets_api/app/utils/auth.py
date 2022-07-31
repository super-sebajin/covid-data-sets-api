from re import U
import main
from models import ApiUser
from datetime import datetime, time, timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, NoneIsAllowedError
from jose import JWTError, jwt
from passlib.context import CryptContext
from . import exceptions
from .database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(DIR))




class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None


class CustomAuth:
    
    _SECRET_KEY: str
    _ALGORITHM: str 
    _ACCESS_TOKEN_EXPIRE_MINUTES: int

    _PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
    _OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token")

    def __init__(self, expire_minutes = 15):
        self._SECRET_KEY = self._generate_secret_key()
        self._ALGORITHM = "HS256"
        self._ACCESS_TOKEN_EXPIRE_MINUTES = expire_minutes
        
    def _generate_secret_key(self):
        import secrets
        return secrets.token_urlsafe(32)

    def _get_password_hash(self, password):
        return self._PWD_CONTEXT.hash(password)

    def _verify_password(self, plain_password, hashed_password):
        return self._PWD_CONTEXT.verify(plain_password, hashed_password)

    def _create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self._SECRET_KEY, algorithm=self._ALGORITHM)        
        return encoded_jwt
    


            

