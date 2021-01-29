import requests
import pandas as pd
from ast import literal_eval
# Import the appropriate estimator class from Scikit-Learn
from sklearn.linear_model import LinearRegression


def population_data_api(year_str):

    # convert to str
    year_str = str(year_str)
  
    # look up how to protect our API keys using environmental variables
    census_api_key = 'ca170bc6585e4b20fe39912a9c403931fa7e8196'

    #make API calls with python
    calledAPI = 'https://api.census.gov/data/' + year_str + '/acs/acs5?get=NAME,B01003_001E&for=place:*&in=state:*&key='+ census_api_key

    #call the API and collect the response
    response = requests.get(calledAPI)

    # this converts the str to the literal type
    result_list = literal_eval(response.text)

    # pop the column header from the result_list
    columns = result_list.pop(0)

    # rename columns
    columns = ['NAME', 'POPULATION', 'state', 'place']
    df = pd.DataFrame(result_list, columns=columns)
    df['YEAR'] = int(year_str)
    return df


def clean_pop_df(df):
  
    # split CITY_STATE for cleaning and feature engineering 
    df[['CITY','STATE']] = df.NAME.str.split(",",expand=True) 

    # clean the leading white space
    df['STATE'] = df.STATE.str.strip(" ")

    # clean city suffixs and endings
    strip_names = [' city', ' borough', ' town', ' village', ' CDP']

    for i in strip_names:
        df['CITY'] = df.CITY.str.replace(i, "")

    # feature engineering for joining key
    df['City, State'] = df.CITY + ", " + df.STATE

    # prep population df for joining
    pop_df = df[['YEAR', 'CITY', 'STATE', 'City, State', 'POPULATION']]

    return pop_df


def fill_10_years_pop_df():
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    years = [str(x) for x in years]
    # dfs = [df_2010, df_2011, df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019]
    
    dfs = []
    for year in years:
        df = population_data_api(year)
        cleaned_df = clean_pop_df(df)
        dfs.append(cleaned_df)
    return dfs


def concat_dfs(all_df):

    # given 10 years of df from 2010 - 2019

    # check shape of one dataset (29514, 5)
    # print(all_df[0].shape)

    # initialize big_df
    big_df = all_df[0]
    # loop and append additional years df
    for i in range(1, 10):
        big_df = pd.concat([big_df, all_df[i]])

    # check size of 10 datasets (295459, 5)
    # print(big_df.shape)

    return big_df


# # Import the appropriate estimator class from Scikit-Learn
# from sklearn.linear_model import LinearRegression
def predict_pop_growth(user_city_state, big_df):

    # get city state from json
    city_state = user_city_state['City, State']

    # filter big_df
    Graph_df = big_df[big_df['City, State']== city_state]

    #2. Instantiate this class
    model = LinearRegression()

    #3. Arrange X features matrix & y target vector
    features = ['YEAR']
    target = 'POPULATION'

    X_train = Graph_df[features]
    y_train = Graph_df[target]
    # print(X_train.shape, y_train.shape)

    #4. Fit the Model
    model.fit(X_train, y_train)

    #5. Apply the model to new data
    from datetime import datetime
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




# MAIN

# this is to fill the database
all_df = fill_10_years_pop_df() # list of dataframes
big_df = concat_dfs(all_df)


# user inpute
user_city_state = {'City, State':'San Francisco, California'}


results = predict_pop_growth(user_city_state, big_df)
print(results) 