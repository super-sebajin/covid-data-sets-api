from sqlalchemy import Column, ForeignKey, String, DateTime, Integer, Boolean
#from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()
class CovidCasesOverTimeUsa(Base):
    __tablename__ = "covid_cases_over_time_usa"
    id = Column(
        UUIDType,
        primary_key=True,
        unique=True,
        nullable=False,
        default=uuid4
    )
    date_stamp = Column(
        DateTime,
        nullable=False,
    )
    count_confirmed = Column(
        Integer,
        nullable=False
    )
    count_death = Column(
        Integer,
        nullable=False
    )
    count_recovered = Column(
        Integer,
        nullable=False
    )
    covid_data_sets_id = Column(
        UUIDType,
        ForeignKey('covid_data_sets.id')
    )
    data_set = relationship('CovidDataSets')

class CovidDataSets(Base):
    __tablename__ = "covid_data_sets"
    id = Column(
        UUIDType,
        primary_key=True,
        unique=True,
        nullable=False,
        default=uuid4
    )
    data_set_name = Column(
        String,
        nullable=False
    )
    data_set_public_url = Column(
        String,
        nullable=False
    )
    data_set_public_url_method = Column(
        String,
        nullable=False
    )
    provider_long_name = Column(
        String,
        nullable=False,
        default=''
    )
    provider_short_name = Column(
        String,
        nullable=False,
        default=''
    )
    
class ApiUser(Base):
    __tablename__ = "api_user"
    id = Column(
        UUIDType,
        nullable=False,
        default=uuid4,
        primary_key=True,
    )
    username = Column(
        String,
        nullable=False
    )
    password = Column(
        String,
        nullable=False
    )
    disabled = Column(
        Boolean,
        nullable=False,
        default=False
    )
