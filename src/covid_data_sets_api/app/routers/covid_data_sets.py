from fastapi import APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware, db
from pydantic import NoneIsAllowedError
from sqlalchemy.sql.expression import delete
from typing import Generic, List
from uuid import UUID
import json
from schema import CovidDataSets as SchemaCovidDataSets
from schema import GenericResponse as SchemaGenericResponse
from schema import CovidDataSets, GenericResponse
from models import CovidDataSets as ModelCovidDataSets


router = APIRouter()

@router.post("/covid_data_set", response_model=SchemaCovidDataSets, tags=["covid_data_sets"])
async def insert_covid_data_set(data_set: CovidDataSets) -> ModelCovidDataSets:
    db_covid_data_set = ModelCovidDataSets(
        data_set_name = data_set.data_set_name,
        data_set_public_url = data_set.data_set_public_url,
        data_set_public_url_method = data_set.data_set_public_url_method,
        provider_long_name = data_set.provider_long_name,
        provider_short_name = data_set.provider_short_name
    )
    db.session.add(db_covid_data_set)
    db.session.commit()
    return db_covid_data_set   

@router.get("/all_covid_data_sets", response_model=List[SchemaCovidDataSets], tags=["covid_data_sets"])
async def all_covid_data_sets() -> List[ModelCovidDataSets]:
    return db.session.query(ModelCovidDataSets).all()

@router.get("/get_covid_data_set_by_id/{id}",  tags=["covid_data_sets"])
async def covid_data_by_id(id: UUID) -> ModelCovidDataSets:
    
    operation = db.session.query(ModelCovidDataSets).filter(ModelCovidDataSets.id == id).first()
    if operation != None:
        return db.session.query(ModelCovidDataSets).filter(ModelCovidDataSets.id == id).first()
    else:
        return GenericResponse(False, f"No record exists for {id}")

@router.delete("/delete_covid_data_set/{id}", tags=["covid_data_sets"])
async def delete_covid_data_set(id: UUID):

    try:
        operation = db.session.query(ModelCovidDataSets).filter(ModelCovidDataSets.id == id).first()
        if operation == None:
            return GenericResponse(False, f"No record exists for {id}")
        else:    
            db.session.commit()
            return GenericResponse(True)
    except Exception as ex: 
        return GenericResponse(False, str(ex))
 
