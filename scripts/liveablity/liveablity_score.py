import pandas as pd 


total = pd.read_csv('https://raw.githubusercontent.com/JeffreyAsuncion/LambdaLabs/main/cityspire-a-ds/Datasets_csv/pop_cc_rr_ws.csv')

#

def crime_liv(df):
  temp_crime = df['crime_rate'] * 33
  temp_crime_liv  = temp_crime / 21000
  df['liv_crime'] = 30 - temp_crime_liv
  
  return df

def rental_liv(df):
  temp_rental = df['rental_rate'] * 33
  df['liv_rental'] = temp_rental / 3529.70
  
  return df 

def walk_liv(df):
  temp_walk = df['walk_score'] * 34
  df['liv_walk'] = temp_walk / 211.14

  return df 

crime_liv(total)
rental_liv(total)
walk_liv(total)

def liv_score(df):
  df['livability_score'] = df['liv_crime'] + df["liv_rental"] + df['liv_walk']
 
  return df

liv_score(total)

total['livability_score'] = total['livability_score'].round(2)

total.drop(total.columns[[6,7,8]], axis=1, inplace=True)