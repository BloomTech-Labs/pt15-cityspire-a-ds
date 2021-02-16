"""Machine learning functions"""
# Import the appropriate estimator class from Scikit-Learn
from sklearn.linear_model import LinearRegression
from datetime import datetime



"""Machine learning functions"""

from fastapi import APIRouter
from sklearn.neighbors import NearestNeighbors
import pandas as pd
from joblib import load
import pickle
from app.data_dict.city_state_json import city_state_2_id_num

router = APIRouter()


# filename = 'app/recommend/recommendation_model.sav'
# model_file = open(filename, 'rb')
# loaded_model = pickle.load(model_file)
# states_pkl = pd.read_pickle('app/recommend/states_dataset.pkl')


# @router.get('/recommend')
# async def suggest_state_ids(city_state : str):
#     '''Returns the list of 10 city_states with features
        
#         for a given city_state, i.e., "Newark, New Jersey"    
    
#         This is a sample response of 2 recommended city_states
        
#         [
#           [
#             {
#               "city_state": "Newark, New Jersey",
#               "id_num": 17089,
#               "population": 283945,
#               "crime_rate": 27.4,
#               "rental_rate": 1466.89,
#               "walk_score": 79
#             }
#           ],
#           [
#             {
#               "city_state": "Chula Vista, California",
#               "id_num": 3151,
#               "population": 280863,
#               "crime_rate": 16.2,
#               "rental_rate": 2477.6,
#               "walk_score": 43
#             }
#           ]
#         ]

#         NOTE: This route will return 10 recommmended city_states                
#     '''

#     # use dictionary to find state_id
#     state_id = city_state_2_id_num[city_state]
    
#     # pass state_id to model 
#     state_index = states_pkl.index[states_pkl['id_num'] == state_id]

#     # use 'state_id' to find state_features
#     state_features = states_pkl.iloc[state_index, 2:].to_numpy()

#     # load pkl NearestNeighbors Model
#     dist, indices = loaded_model.kneighbors(state_features)

#     # list of 10 recommended state_id
#     recommended_list = list(states_pkl.loc[indices[0], 'id_num'])

#     # list of state_id with respective state feature
#     results = []
#     for i in range(len(recommended_list)):
#       r_list = states_pkl[states_pkl['id_num']==recommended_list[i]]
#       r = r_list.to_dict('records')
#       results.append(r)
    
#     return results



