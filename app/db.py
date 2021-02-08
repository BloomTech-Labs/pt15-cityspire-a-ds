"""Database functions"""

import os

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy

from app.population import predict_pop_growth
import requests
import pandas as pd
from ast import literal_eval
# Import the appropriate estimator class from Scikit-Learn
from sklearn.linear_model import LinearRegression
import sqlite3

from .models import Pop_Table
#
#
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

from .schemas import Pop_History, Predict_Pop

models.Base.metadata.create_all(bind=engine)
#
#
router = APIRouter()


# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# this is conflicts with the one i added above
async def get_db() -> sqlalchemy.engine.base.Connection:
    """Get a SQLAlchemy database connection.
    
    Uses this environment variable if it exists:  
    DATABASE_URL=dialect://user:password@host/dbname

    Otherwise uses a SQLite database for initial local development.
    """
    load_dotenv()
    # database_url = os.getenv('DATABASE_URL', default='sqlite:///temporary.db')
    database_url = os.getenv('DATABASE_URL', default='sqlite:///app/pop_db.sqlite3')
    engine = sqlalchemy.create_engine(database_url)
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()


@router.get('/info')
async def get_url(connection=Depends(get_db)):
    """Verify we can connect to the database, 
    and return the database URL in this format:

    dialect://user:password@host/dbname

    The password will be hidden with ***
    """
    url_without_password = repr(connection.engine.url)
    return {'database_url': url_without_password}




#
# Dummy Endpoints
#


@router.get('/call_population')
async def predict():
    """
    Predict population in Newark, New Jersey.
    {
        "city_state": "Newark, New Jersey",
        "year": 2012
    }

    """
    
    return {
            "population": 276478,
            "city_state": "Newark, New Jersey",
            "year": 2012,
            "id_num": 17634
            }


@router.get('/population_history/')
async def predict():
    """
    collect population in Newark, New Jersey.
    {
        "city_state": "Newark, New Jersey",
        "year": 2022
    }

    """
    results = [
                {
                    "population": 274674,
                    "city_state": "Newark, New Jersey",
                    "year": 2010,
                    "id_num": 17130
                },
                {
                    "population": 275512,
                    "city_state": "Newark, New Jersey",
                    "year": 2011,
                    "id_num": 16283
                },
                {
                    "population": 276478,
                    "city_state": "Newark, New Jersey",
                    "year": 2012,
                    "id_num": 15634
                },
                {
                    "population": 277357,
                    "city_state": "Newark, New Jersey",
                    "year": 2013,
                    "id_num": 16044
                },
                {
                    "population": 278750,
                    "city_state": "Newark, New Jersey",
                    "year": 2014,
                    "id_num": 15513
                },
                {
                    "population": 279793,
                    "city_state": "Newark, New Jersey",
                    "year": 2015,
                    "id_num": 22111
                },
                {
                    "population": 280139,
                    "city_state": "Newark, New Jersey",
                    "year": 2016,
                    "id_num": 22848
                },
                {
                    "population": 282803,
                    "city_state": "Newark, New Jersey",
                    "year": 2017,
                    "id_num": 21428
                },
                {
                    "population": 280463,
                    "city_state": "Newark, New Jersey",
                    "year": 2018,
                    "id_num": 3135
                },
                {
                    "population": 281054,
                    "city_state": "Newark, New Jersey",
                    "year": 2019,
                    "id_num": 25726
                }
                ]
    return results

#
# Dummy Endpoints
#






#
# This code works with SQLITE DB
#
# @router.get('/pop_query/{year}/{city_state}')
# async def query_pop(year: int, city_state: str, db: Session=Depends(get_db)):

#     results = crud.get_pop_predict_model(db, year, city_state)
#     if results == []:
#         results = {"error": 123}
#     return results


# @router.get('/pop_query_predict_10/{city_state}')
# async def predict_pop_model_10(city_state: str, db: Session=Depends(get_db)):

#     results = crud.pop_predict_model_all(db, city_state)
    
#     if results == []:
#         results = {"error": 123}
#     return results
#
# This code works with SQLITE DB
#
