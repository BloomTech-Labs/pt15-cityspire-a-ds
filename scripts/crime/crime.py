import pandas as pd
import numpy as np


crime_2019 = pd.read_excel('./data/Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2019.xls')
crime_2018 = pd.read_excel('./data/Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2018.xls')
crime_2017 = pd.read_excel('./data/Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2017.xls')
crime_2016 = pd.read_excel('./data/Table_6_Offenses_Known_to_Law_Enforcement_by_State_by_City_2016.xls')
crime_2015 = pd.read_excel('./data/Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2015.xls')
crime_2014 = pd.read_excel('./data/table-8.xls')


def clean_2019(df):
        '''
        simple cleaning function to preprcess 2019 data to for modeling
        df: input data frame
        '''
        # deleting last 8 rows due to useles info
        df = df.drop(df.tail(8).index)

        # front fill states 
        df['State'] = df['State'].fillna(method='ffill')
        temp = df['State'].str.split("-", n=1, expand=True)
        df['State'] = temp[0]

        # Alabama naming fix
        df['State'] = df['State'].str.replace('ALABAMA3', 'ALABAMA')

        df.columns = df.columns.str.replace('\n',' ' )
        df = df.rename(columns={'Arson2':'Arson'})

        # droping unwanted columns
        df.drop(['Rape1', 'Murder and nonnegligent manslaughter', 'Robbery', 'Aggravated assault', 
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
        df['year'] = 2019

        # Add City, State
        df['City, State'] = df.City + ", " + df.State

        print(df.head(3))

        return df

def clean_2018(df):
        '''
        simple cleaning function to preprcess 2018 data to for modeling
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

        # Add City, State
        df['City, State'] = df.City + ", " + df.State

        print(df.head(3))

        return df

def clean_2017(df):
        
        '''
        simple cleaning function to preprcess 2017 data to for modeling
        df: input data frame
        '''
        # deleting last 10 rows due to useles info
        df = df.drop(df.tail(10).index)

        # front fill states 
        df['State'] = df['State'].fillna(method='ffill')
        temp = df['State'].str.split("-", n=1, expand=True)
        df['State'] = temp[0]
        
        # fix formating of headers
        df.columns = df.columns.str.replace('\n',' ' )

        # # droping unwanted columns
        drop_list = ['State', 'City', 'Population', 'Violent crime', 'Property crime']
        df = df.drop(df.columns.difference(drop_list), axis=1)

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
        df['year'] = 2017

        # Add City, State
        df['City, State'] = df.City + ", " + df.State

        print(df.head(3))

        return df

def clean_2016(df):
        
        '''
        simple cleaning function to preprcess 2016 data to for modeling
        df: input data frame
        '''

        # deleting last 10 rows due to useles info
        df = df.drop(df.tail(11).index)

        # front fill states 
        df['State'] = df['State'].fillna(method='ffill')
        temp = df['State'].str.split("-", n=1, expand=True)
        df['State'] = temp[0]
        
        # fix formating of headers
        df.columns = df.columns.str.replace('\n',' ' )

        # # droping unwanted columns
        drop_list = ['State', 'City', 'Population', 'Violent crime', 'Property crime']
        df = df.drop(df.columns.difference(drop_list), axis=1)

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
        df['year'] = 2016

        # Add City, State
        df['City, State'] = df.City + ", " + df.State

        print(df.head(3))

        return df

def clean_2015(df):

        '''
        simple cleaning function to preprcess 2015 data to for modeling
        df: input data frame
        '''

        # deleting last 10 rows due to useles info
        df = df.drop(df.tail(10).index)

        # front fill states 
        df['State'] = df['State'].fillna(method='ffill')
        temp = df['State'].str.split("-", n=1, expand=True)
        df['State'] = temp[0]
        
        # NJ naming fix
        df['State'] = df['State'].str.replace('NEW JERSEY9', 'NEW JERSEY')

        # fix formating of headers
        df.columns = df.columns.str.replace('\n',' ' )

        # # droping unwanted columns
        drop_list = ['State', 'City', 'Population', 'Violent crime', 'Property crime']
        df = df.drop(df.columns.difference(drop_list), axis=1)

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
        df['year'] = 2015

        # Add City, State
        df['City, State'] = df.City + ", " + df.State

        print(df.head(3))

        return df

def clean_2014(df): 

        '''
        simple cleaning function to preprcess 2014 data to for modeling
        df: input data frame
        '''

        # deleting last 17 rows due to useles info
        df = df.drop(df.tail(17).index)

        # front fill states 
        df['State'] = df['State'].fillna(method='ffill')
        temp = df['State'].str.split("-", n=1, expand=True)
        df['State'] = temp[0]
        
        # GA naming fix
        df['State'] = df['State'].str.replace('GEORGIA7', 'GEORGIA')

        # fix formating of headers
        df.columns = df.columns.str.replace('\n',' ' )

        # # droping unwanted columns
        drop_list = ['State', 'City', 'Population', 'Violent crime', 'Property crime']
        df = df.drop(df.columns.difference(drop_list), axis=1)

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
        df['year'] = 2014

        # Add City, State
        df['City, State'] = df.City + ", " + df.State

        print(df.head(3))

        return df
        

crime_2014 = clean_2014(crime_2014)
crime_2015 = clean_2015(crime_2015)
crime_2016 = clean_2016(crime_2016)
crime_2017 = clean_2017(crime_2017)
crime_2018 = clean_2018(crime_2018)
crime_2019 = clean_2019(crime_2019)

# create csv's
crime_2019.to_csv('crime_2019.csv')
crime_2018.to_csv('crime_2018.csv')
crime_2017.to_csv('crime_2017.csv')
crime_2016.to_csv('crime_2016.csv')
crime_2015.to_csv('crime_2015.csv')
crime_2014.to_csv('crime_2014.csv')

