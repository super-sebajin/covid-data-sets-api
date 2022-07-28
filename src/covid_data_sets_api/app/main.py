import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import CovidDataSets as SchemaCovidDataSets
from schema import CovidCasesOverTimeUsa as SchemaCovidCasesOverTimeUsa

from schema import CovidDataSets
from schema import CovidCasesOverTimeUsa

from models import CovidDataSets as ModelCovidDataSets
from models import CovidCasesOverTimeUsa as ModelCovidCasesOverTimeUsa

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
async def root():
    return {"message":"Welcome to the Covid Data Sets api"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)