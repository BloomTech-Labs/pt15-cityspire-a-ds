import pandas as pd 


crime = pd.read_csv('./csvs/combined_crime.csv')

# drop City and State
crime = crime.drop(crime.columns[[0, 1]], axis=1)

# remove cities/ that have no population
crime = crime[crime['Population'].notnull()]

def crime_per_capita(row, number_of_people):
    try:
        total_crimes = row['Violent crime'] + row['Property crime']
        population = row['Population']
        count = (total_crimes/population)*number_of_people

    except ZeroDivisionError:
        count = 0

    return count

crime['crime_per_1000'] = crime.apply(crime_per_capita, args=(1000,), axis=1)

# get national average
total_population = crime['Population'].sum()
total_crimes =+ crime['Violent crime'].sum() + crime['Property crime'].sum()
national_average_per_cap = (total_crimes/total_population)*1000

# add column of diff to national average
def compute_diff(row):
    diff = row['crime_per_1000'] - national_average_per_cap
    return diff

crime['diff_of_national_average'] = crime.apply(compute_diff, axis=1)

# add column of percent diff compared to national average
def compute_percent(row):
    percent = (row['crime_per_1000']/national_average_per_cap)*100
    if percent > 100:
        return "+" + str(int(percent-100)) + "%"
    return "-" + str(100 - int(percent)) + "%"

crime['percent_diff_national'] = crime.apply(compute_percent, axis=1)

print(crime.head(3))