import uvicorn
from fastapi import FastAPI, Depends
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from routers import covid_data_sets, users
from fastapi import Depends, FastAPI, HTTPException, status
import os
from uuid import uuid4
from dotenv import load_dotenv, find_dotenv
from utils.auth import CustomAuth, Token, TokenData
from jose import jwt, JWTError

load_dotenv(find_dotenv())

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])
app.include_router(covid_data_sets.router)
app.include_router(users.router)

#auth=CustomAuth()

@app.get("/", tags=["root"])
async def root():
    return {"message":"Welcome to the Covid Data Sets api"}

# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)