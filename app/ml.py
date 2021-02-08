"""Machine learning functions"""
# Import the appropriate estimator class from Scikit-Learn
from sklearn.linear_model import LinearRegression
from datetime import datetime



from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import pandas as pd

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .models import Pop_Table
import simplejson as json



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

#/{user_city_state}')
@router.get('/ML_pop_predict/{user_city_state}')
async def ML_predict_pop_growth_route(user_city_state, db: Session=Depends(get_db)): 
    
    # NOTE input in form {'City_State' : 'San Francisco, California'}

    # # get city state from json
    # city_state = user_city_state['City_State']
    
    # for 2021.02.03 test
    city_state = user_city_state 

    # https://stackoverflow.com/questions/40973211/convert-list-of-dictionaries-to-a-dataframe 
    list_dict = crud.pop_predict_model_all(db, city_state)
    # returns a json object 

    Graph_df = pd.read_sql_query(list_dict, con=db)
    print(Graph_df.shape, Graph_df.columns)
    return list_dict  
    
    # data = json.dumps(list_dict)
    # print(data)
    # print(list_dict)
    

    # Graph_df = pd.DataFrame.from_records(list_dict)
    # print(Graph_df.shape, Graph_df.columns)
    # return list_dict


    #2. Instantiate this class
    model = LinearRegression()

    #3. Arrange X features matrix & y target vector
    # make sure to match the list of dict [columns]
    features = ['year']
    target = 'population'

    X_train = Graph_df[features]
    y_train = Graph_df[target]

    #4. Fit the Model
    model.fit(X_train, y_train)

    #5. Apply the model to new data
    # from datetime import datetime
    today = datetime.today()

    # this year prediction
    this_year = today.year
    test_features =[this_year]
    X_test = [test_features]
    y_pred_this_year = model.predict(X_test)
    y_pred_this_year = round(y_pred_this_year[0], 0)
    this_label = 'pop_'+ str(this_year)

    # last year prediction
    last_year = this_year - 1
    test_features =[last_year]
    X_test = [test_features]
    y_pred_last_year = model.predict(X_test)
    y_pred_last_year = round(y_pred_last_year[0],0)
    last_label = 'pop_'+ str(last_year)

    # calculate percent_pop_growth
    percent_pop_growth = (y_pred_this_year - y_pred_last_year)/y_pred_last_year * 100
    percent_pop_growth = round(percent_pop_growth,2)

    return {last_label: y_pred_last_year, this_label: y_pred_this_year, 'percent_pop_growth': percent_pop_growth}