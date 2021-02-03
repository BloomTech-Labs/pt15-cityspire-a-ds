"""Machine learning functions"""
# Import the appropriate estimator class from Scikit-Learn
from sklearn.linear_model import LinearRegression
from datetime import datetime
from app.population import predict_pop_growth

from fastapi import APIRouter

import pandas as pd

router = APIRouter()

#/{user_city_state}')
@router.post('/ML_pop_predict/{user_city_state}')
async def ML_predict_pop_growth_route(user_city_state): 
    results = predict_pop_growth(user_city_state)
    return results