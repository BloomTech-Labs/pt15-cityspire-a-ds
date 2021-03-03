# KnownDefects

The DS API works well in exception to the following cases

1. mispelled city, states
2. city, states that are not represented in the dataset

The rental prediction is good for about 6 months out. The model breaks down after predicting on predictions. It would be wise to perpetually feed new accurate data to the Corrected_Zillow.csv dataset


The join dataset for the NearestNeighbors model is not updated with the rental prediction above please see the CiryspireDatasetJoin.ipynb to update the join dataset. Then the recommendation_model.sav and states_dataset.pkl needs to be pickled and 
save in the /app/recommend