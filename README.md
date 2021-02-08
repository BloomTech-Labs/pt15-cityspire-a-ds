# Labs DS template

[Docs](https://docs.labs.lambdaschool.com/data-science/)

2021.01.27 - JA
- added request to pipfile - using 'pipenv install requests'
- added pandas to pipfile - using 'pipenv install pandas'
- no need to add ast to pipfile - already exists
- added sklearn to pipfile - using 'pipenv install sklearn'

2021.01.28 - JA
- added SQLAlchemy to pipfile - using 'pipenv install SQLAlchemy'

2021.01.29 - JA
- to run fastapi app - 'uvicorn app.main:app --reload'
- reminder when you open folder
    - pipenv shell
    - code .
- Reminder when you change the pipenv install --dev
    - you have to delete the piplock file
    - they do not write over or replace
    - you must do it manually
- https://fastapi.tiangolo.com/advanced/testing-database/
- https://datacarpentry.org/python-ecology-lesson/09-working-with-sql/index.htmlhh
- SQLITE test db works with population.py
2021.01.30
- created .env file for credentials
- load_dotenv() and os.getenv() to call credentials



2021.02.02
https://fastapi.tiangolo.com/tutorial/sql-databases/
- database.py
- models.py
- crud.py
- main part 



- import Pydantics Base Model - https://fastapi.tiangolo.com/tutorial/body/

class UserInput(Base Model):
    crime_rate :  float
    rental_rate : float
    population : int


Database call not returning .all() due to primary key error, need to index and add column

    # save the big_df as a csv
    big_df.to_csv('app/pop_2010_2019.csv', sep=',', index=True) # changed to True

        sql = """
        CREATE TABLE pop_2010_2019 (
            id INTEGER,
            year INTEGER,
            city_state TEXT,
            population INTEGER,
            primary key(id)
        ) """

I am currently working on a FastAPI app 
that is calling data from Sqlite db and SQLAlchemy is 
returning objects instead of the data. Please advise

Need to write a __repr__(self) for db class

- pipenv install simplejson
- import simplejson as json