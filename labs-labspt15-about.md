# Development Description

1. The Population dataset 
    contains predicted values for the year 2021. This prediction was based on ten years of population data from the census.gov API for the years 2010 to 2019.

* census api key is available in the link below
* https://api.census.gov/data/key_signup.html


2. The Joined dataset 
    used for the recommendation model is a Full Join of all the datasets.

* Population data set has a shape of (29,626, 3)  
* Crime Rate dataset has a shape of (9248, 4)
* Rental Rates dataset has a shape of (104, 4) 
* Walk Score dataset has a shape of (2500, 5)

    Missing values were filled with the feature’s average value of  a given state if the state doesn't have an average the national average will be used for that given feature.


3. Rental Dataset:
    The Corrected_Zillow.csv has 2263  observations and 92 features. After using an interpolation method to correct Nans, some NaN values had to be manually entered. By taking the nearest neighbors ( up to 4) average. See the notebook Rental_Predictions_Zillow.ipynb for details. The predictions for future years are 12 month averages for that particular year.