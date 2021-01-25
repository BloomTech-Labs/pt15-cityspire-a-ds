import pandas as pd
import  numpy as np
import string


# read in csv
crime = pd.read_csv('./crime.csv')

## pre-processing of data 

# removing subscripts numbers from text
crime['City'] = crime.City.str.replace('\d+', '')

# lowercasing columns name and values
crime = crime.rename(columns=str.lower)
crime = crime.applymap(lambda s:s.lower() if type(s) == str else s)

# replaceing missing values to 0
crime['violent crime'] = crime['violent crime'].replace(np.nan,0)
crime['property crime'] = crime['property crime'].replace(np.nan,0)


crime.to_csv('crime_cleaned.csv')