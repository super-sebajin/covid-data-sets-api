from fastapi import APIRouter
from fastapi_sqlalchemy import db
from sqlalchemy.sql.expression import delete
from typing import Union, List
from uuid import UUID, uuid4
from schema import CovidDataSets as SchemaCovidDataSets
from schema import GenericResponse as SchemaGenericResponse
from schema import CovidDataSets, GenericResponse
from models import CovidDataSets as ModelCovidDataSets


router = APIRouter()


@router.post(
    "/covid_data_set",
    response_model=SchemaCovidDataSets,
    tags=["covid_data_sets"]
)
async def insert_covid_data_set(data_set: CovidDataSets):
    db_covid_data_set = ModelCovidDataSets(
        id = uuid4(),
        data_set_name=data_set.data_set_name,
        data_set_public_url=data_set.data_set_public_url,
        data_set_public_url_method=data_set.data_set_public_url_method,
        provider_long_name=data_set.provider_long_name,
        provider_short_name=data_set.provider_short_name
    )
    db.session.add(db_covid_data_set)
    db.session.commit()
    return db_covid_data_set


@router.get(
    "/all_covid_data_sets",
    response_model=List[SchemaCovidDataSets],
    tags=["covid_data_sets"]
)
async def all_covid_data_sets():
    return db.session.query(ModelCovidDataSets).all()


@router.get(
    "/get_covid_data_set_by_id/{id}",
    response_model=Union[SchemaGenericResponse, SchemaCovidDataSets],
    tags=["covid_data_sets"]
)
async def covid_data_by_id(id: UUID):

    operation = db.session.query(ModelCovidDataSets).filter(
        ModelCovidDataSets.id == id)
    if operation.first() != None:
        return db.session.query(ModelCovidDataSets).filter(ModelCovidDataSets.id == id).first()
    else:
        return GenericResponse(False, f"No record exists for {id}")


@router.delete(
    "/delete_covid_data_set/{id}",
    response_model=SchemaGenericResponse,
    tags=["covid_data_sets"]
)
async def delete_covid_data_set(id: UUID):
    
    row = db.session.query(ModelCovidDataSets).filter(
        ModelCovidDataSets.id == id)
    if row.first() == None:
        return GenericResponse(False, f"No record exists for {id}")
    else:
        row.delete()
        db.session.commit()
        return GenericResponse(True)
    