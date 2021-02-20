"""Database functions"""

import os

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy
from app.data_dict.predict_json import predict_2021
from app.data_dict.city_state_json import city_state_2_id_num
import pandas as pd

router = APIRouter()

states_pkl = pd.read_pickle('app/recommend/states_dataset.pkl')

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

@router.get('/state_id')
async def return_city_state(city_state: str):
    '''Returns the state_id

        for a given city_state, i.e., "Newark, New Jersey"    
    
        {"Newark, New Jersey" : 18127 }
                
    '''
    return {"id_num" : city_state_2_id_num[city_state]}


@router.get('/predict')
async def predict_city_state(city_state: str):
    '''Returns the predicted values for a given state

        for a given city_state, i.e., "Newark, New Jersey"    
    
        {
        "id_num": 17089,

        "population": 283945,

        "crime_rate": 27.4,

        "rental_rate": 1466.89,
        
        "walk_score": 79
        }
                
    '''
    return predict_2021[city_state]

@router.get('/livability')
async def calculate_livability(city_state:str, crime_percent:float, rental_percent:float):
    '''
        Returns the Livability Score for a city_state
            { "livability_score" : 54.06 }

            params : 
                city_state - "Newark, New Jersey"
                crime_percent - 40.0
                rental_percent - 40.0

                walk_percent = 100 - crime_percent - rental_percent 
    '''
    #calculate walk_score percentage in livability
    walk_percent = 100 - crime_percent - rental_percent

    a = states_pkl[states_pkl["city_state"]== city_state]
    # convert a dataframe to a list 
    A = a.values.tolist()

    temp_crime = A[0][3] * crime_percent
    temp_crime_liv  = temp_crime / 21000   #21000 is the max value crime rate
    liv_crime = 30 - temp_crime_liv

    temp_rental = A[0][4] * rental_percent
    liv_rental = temp_rental / 3529.70 # 3529 is the max value for rental rate

    temp_walk = A[0][5] * walk_percent
    liv_walk = temp_walk / 211.1 # 211.1 is the max value for walk score

    livability_score = round((liv_crime + liv_rental + liv_walk),2)

    return {"livability_score" : livability_score}