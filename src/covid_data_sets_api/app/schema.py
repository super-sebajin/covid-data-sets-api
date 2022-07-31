import datetime
import json
from pydantic import BaseModel

from typing import Optional
from uuid import UUID, uuid4
from pydantic.dataclasses import dataclass
class CovidDataSets(BaseModel):
    id: Optional[UUID]
    data_set_name: str
    data_set_public_url: str
    data_set_public_url_method: str
    provider_long_name: str
    provider_short_name: str

    class Config:
        orm_mode = True
    
class CovidCasesOverTimeUsa(BaseModel):
    date_stamp: datetime.datetime
    count_confirmed: int
    count_death: int
    count_recovered: int
    covid_data_sets_id: UUID   

    class Config:
        orm_mode = True

class ApiUser(BaseModel):
    id: Optional[UUID]
    username: str
    password: str

    class Config:
        orm_mode=True

@dataclass
class GenericResponse:
    success: bool
    errors: Optional[str]

    def __init__(self, success, errors = None):
        self.success = success
        self.errors = errors

  


    

   


  