import pandas as pd
import numpy as np


crime_2018 = pd.read_excel('./data/Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2018.xls')

def clean_2018(df):
        '''
        simple cleaning function to preprcess data to for modeling
        df: input data frame
        '''
        # deleting last 10 rows due to useles info
        df = df.drop(df.tail(10).index)

        # front fill states 
        df['State'] = df['State'].fillna(method='ffill')
        temp = df['State'].str.split("-", n=1, expand=True)
        df['State'] = temp[0]

        # state naming fixing
        df['State'] = df['State'].str.replace('IOWA7', 'IOWA')
        df['State'] = df['State'].str.replace('NORTH CAROLINA8', 'NORTH CAROLINA')

        df.columns = df.columns.str.replace('\n',' ' )

        # droping unwanted columns
        df.drop(['Rape', 'Murder and nonnegligent manslaughter', 'Robbery', 'Aggravated assault', 
                'Burglary','Motor vehicle theft', 'Arson', 'Larceny- theft'], axis=1, inplace=True)

        # lowercasing whole df
        df = df.applymap(lambda s:s.lower() if type(s) == str else s)

        # dealing with NaN's
        zeros = ['Violent crime', 'Property crime']
        df[zeros] = df[zeros].fillna(value=0)


        # removing unessary text from cities 
        df['City'] = df['City'].str.replace(' County Police Department', '')
        df['City'] = df['City'].str.replace(' Police Department', '')
        df['City'] = df['City'].str.replace(' County', '')
        df['City'] = df['City'].str.replace('7', '')
        df['City'] = df['City'].str.replace('5', '')
        df['City'] = df['City'].str.replace('3', '')
        df['City'] = df['City'].str.replace("'s", '')

        # adding year to df
        df['year'] = 2018

        print(df.head(3))

        return df

crime_2018 = clean_2018(crime_2018)

# create csv
# crime_2018.to_csv('crime_2018')

