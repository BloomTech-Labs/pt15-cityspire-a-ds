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

models.Base.metadata.create_all(bind=engine)
#
#
router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



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


@router.get('/pop_query/{year}/{city_state}')
async def query_pop(year: int, city_state: str, db: Session=Depends(get_db)):

    results = crud.get_pop_predict_model(db, year, city_state)
    if results == []:
        results = {"error": 123}
    return results


@router.get('/pop_query_predict_10/{city_state}')
async def predict_pop_model_10(city_state: str, db: Session=Depends(get_db)):

    results = crud.pop_predict_model_all(db, city_state)
    
    if results == []:
        results = {"error": 123}
    return results