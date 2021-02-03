from typing import List, Optional

from pydantic import BaseModel

# for recommendation model
class User_Recommend(BaseModel):
    crime_rate : float
    rental_rate : float
    population : int

# for query population of year, city_state
class Query_Population(BaseModel):
    year : int
    city_state : str

# for population prediction of year and city_state
class Predict_Population(BaseModel):
    year : int
    city_state : str
