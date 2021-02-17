"""Database functions"""

import os

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy
from app.data_dict.predict_json import predict_2021
from app.data_dict.city_state_json import city_state_2_id_num


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