import datetime
import json
from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4
from pydantic.dataclasses import dataclass
class CovidDataSets(BaseModel):
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


class GenericResponse:
    success: bool
    errors: Optional[str]

    def __init__(self, success, errors = None):
        self.success = success
        self.errors = errors

    # def __iter__(self):
    #     yield from {
    #         "success": self.success, 
    #         "errors": self.errors
    #     }.items()

    # def __str__(self):
    #     return json.dumps(dict(self), ensure_ascii=True)

    # def __repr__(self):
    #     return self.__str__()    


    

   


  