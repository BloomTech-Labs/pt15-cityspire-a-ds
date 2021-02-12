import pandas as pd


walk = pd.read_csv('./walk.csv')


# add state names instead of abbv
walk["State"] = walk['State'].str.replace('AK', 'Alaska', regex=False)
walk["State"] = walk['State'].str.replace('AL', 'Alabama', regex=False)
walk["State"] = walk['State'].str.replace('AR', 'Arkansas', regex=False)
walk["State"] = walk['State'].str.replace('AS', 'American Samoa', regex=False)
walk["State"] = walk['State'].str.replace('AZ', 'Arizona', regex=False)
walk["State"] = walk['State'].str.replace('CA', 'California', regex=False)
walk["State"] = walk['State'].str.replace('CO', 'Colorado', regex=False)
walk["State"] = walk['State'].str.replace('CT', 'Connecticut', regex=False)
walk["State"] = walk['State'].str.replace('DC', 'District of Columbia', regex=False)
walk["State"] = walk['State'].str.replace('DE', 'Delaware', regex=False)
walk["State"] = walk['State'].str.replace('FL', 'Florida', regex=False)
walk["State"] = walk['State'].str.replace('GA', 'Georgia', regex=False)
walk["State"] = walk['State'].str.replace('GU', 'Guam', regex=False)
walk["State"] = walk['State'].str.replace('HI', 'Hawaii', regex=False)
walk["State"] = walk['State'].str.replace('IA', 'Iowa', regex=False)
walk["State"] = walk['State'].str.replace('ID', 'Idaho', regex=False)
walk["State"] = walk['State'].str.replace('IL', 'Illinois', regex=False)
walk["State"] = walk['State'].str.replace('IN', 'Indiana', regex=False)
walk["State"] = walk['State'].str.replace('KS', 'Kansas', regex=False)
walk["State"] = walk['State'].str.replace('KY', 'Kentucky', regex=False)
walk["State"] = walk['State'].str.replace('LA', 'Louisiana', regex=False)
walk["State"] = walk['State'].str.replace('MA', 'Massachusetts', regex=False)
walk["State"] = walk['State'].str.replace('MD', 'Maryland', regex=False)
walk["State"] = walk['State'].str.replace('ME', 'Maine', regex=False)
walk["State"] = walk['State'].str.replace('MI', 'Michigan', regex=False)
walk["State"] = walk['State'].str.replace('MN', 'Minnesota', regex=False)
walk["State"] = walk['State'].str.replace('MO', 'Missouri', regex=False)
walk["State"] = walk['State'].str.replace('MP', 'Northern Mariana Islands', regex=False)
walk["State"] = walk['State'].str.replace('MS', 'Mississippi', regex=False)
walk["State"] = walk['State'].str.replace('MT', 'Montana', regex=False)
walk["State"] = walk['State'].str.replace('NA', 'National', regex=False)
walk["State"] = walk['State'].str.replace('NC', 'North Carolina', regex=False)
walk["State"] = walk['State'].str.replace('ND', 'North Dakota', regex=False)
walk["State"] = walk['State'].str.replace('NE', 'Nebraska', regex=False)
walk["State"] = walk['State'].str.replace('NH', 'New Hampshire', regex=False)
walk["State"] = walk['State'].str.replace('NJ', 'New Jersey', regex=False)
walk["State"] = walk['State'].str.replace('NM', 'New Mexico', regex=False)
walk["State"] = walk['State'].str.replace('NV', 'Nevada', regex=False)
walk["State"] = walk['State'].str.replace('NY', 'New York', regex=False)
walk["State"] = walk['State'].str.replace('OH', 'Ohio', regex=False)
walk["State"] = walk['State'].str.replace('OK', 'Oklahoma', regex=False)
walk["State"] = walk['State'].str.replace('OR', 'Oregon', regex=False)
walk["State"] = walk['State'].str.replace('PA', 'Pennsylvania', regex=False)
walk["State"] = walk['State'].str.replace('PR', 'Puerto Rico', regex=False)
walk["State"] = walk['State'].str.replace('RI', 'Rhode Island', regex=False)
walk["State"] = walk['State'].str.replace('SC', 'South Carolina', regex=False)
walk["State"] = walk['State'].str.replace('SD', 'South Dakota', regex=False)
walk["State"] = walk['State'].str.replace('TN', 'Tennessee', regex=False)
walk["State"] = walk['State'].str.replace('TX', 'Texas', regex=False)
walk["State"] = walk['State'].str.replace('UT', 'Utah', regex=False)
walk["State"] = walk['State'].str.replace('VA', 'Virginia', regex=False)
walk["State"] = walk['State'].str.replace('VI', 'Virgin Islands', regex=False)
walk["State"] = walk['State'].str.replace('VT', 'Vermont', regex=False)
walk["State"] = walk['State'].str.replace('WA', 'Washington', regex=False)
walk["State"] = walk['State'].str.replace('WI', 'Wisconsin', regex=False)
walk["State"] = walk['State'].str.replace('WV', 'West Virginia', regex=False)
walk["State"] = walk['State'].str.replace('WY', 'Wyoming', regex=False)


# get rid of first column that is unwanted
walk = walk.drop(['Unnamed: 0'], axis=1)

# add city_state and drop unwanted columns
walk['city_state'] = walk['City'] + ',' + ' ' + walk['State']
walk = walk.drop(columns=['City', 'State', 'Zip Code', 'Population'])

# fix nulls in Transit Scores
walk["Transit Score"] = walk['Transit Score'].str.replace('--', '0', regex=False)



print(walk.head(4))

