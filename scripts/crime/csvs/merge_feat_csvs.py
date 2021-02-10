import pandas as pd


crime_2019 = pd.read_csv('./crime_feat_2019.csv')
crime_2018 = pd.read_csv('./crime_feat_2018.csv')
crime_2017 = pd.read_csv('./crime_feat_2017.csv')
crime_2016 = pd.read_csv('./crime_feat_2016.csv')
crime_2015 = pd.read_csv('./crime_feat_2015.csv')
crime_2014 = pd.read_csv('./crime_feat_2014.csv')

frames = [crime_2019, crime_2018, crime_2017, crime_2016, crime_2015, crime_2014]

combined_crime = pd.concat(frames)

print(combined_crime.head(4))