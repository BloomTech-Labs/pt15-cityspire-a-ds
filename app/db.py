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


router = APIRouter()


async def get_db() -> sqlalchemy.engine.base.Connection:
    """Get a SQLAlchemy database connection.
    
    Uses this environment variable if it exists:  
    DATABASE_URL=dialect://user:password@host/dbname

    Otherwise uses a SQLite database for initial local development.
    """
    load_dotenv()
    database_url = os.getenv('DATABASE_URL', default='sqlite:///temporary.db')
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


@router.get('/pop_predict')
async def predict_pop_growth_route(user_city_state):
    # # user input
    # user_city_state = {'City, State':'San Francisco, California'}


    results = predict_pop_growth(user_city_state)
    return results 

# # MAIN
# # user inpute
# user_city_state = {'City, State':'San Francisco, California'}

# all_df = fill_10_years_pop_df() # list of dataframes
# big_df = concat_dfs(all_df)
# results = predict_pop_growth(user_city_state, big_df)
# print(results) 