import datetime
from pydantic import BaseModel
from uuid import UUID, uuid4
class CovidDataSets(BaseModel):
    id: UUID
    data_set_name: str
    data_set_public_url: str
    data_set_public_url_method: str
    provider_long_name: str
    provider_short_name: str

    class Config:
        orm_mode = True
    
class CovidCasesOverTimeUsa(BaseModel):
    id: UUID
    date_stamp: datetime.datetime
    count_confirmed: int
    count_death: int
    count_recovered: int
    covid_data_sets_id: UUID   

    class Config:
        orm_mode = True