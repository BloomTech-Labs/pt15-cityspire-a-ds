import pandas as pd


us_state_abbrev = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS',
                   'KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC',
                   'ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']


df = pd.DataFrame()

for i in us_state_abbrev:
    df_i = pd.read_html('https://www.walkscore.com/' + i)[0]
    df_i['State'] = i
    df = pd.concat([df, df_i])

print(df.head())