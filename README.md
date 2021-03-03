# Labs DS API 

how to use DS API

1. To find state_id of a city, state 

* for city_state = 'Newark, New Jersey'

    app_url/state_id?city_state=Newark%2C%20New%20Jersey

* Response body
    
    {
    "id_num": 17089
    }


2. to predict the values for population, crime rate, rental rate, and walk score.

* for city_state = 'Newark, New Jersey' 

    app_url/predict?city_state=Newark%2C%20New%20Jersey

* 	Response body

    {
    "id_num": 17089,
    "population": 283945,
    "crime_rate": 27.4,
    "rental_rate": 1466.89,
    "walk_score": 79
    }


3. to calculate the livability for a city, state

* for a city_state = 'Newark, New Jersey', crime_percent - 40.0,   rental_percent - 40.0

    app_url/livability?city_state=Newark%2C%20New%20Jersey&crime_percent=40.0&rental_percent=40.0

* 	Response body

    {
    "livability_score": 54.06
    }


4. to generate list of recommended city, states

* for a population = 200000, crime_rate = 20, rental_rate = 1500, walk_score = 50

    app_url/recommend?population=20000&crime_rate=20&rental_rate=1500&walk_score=50

* Response body

    [
    [
        {
        "city_state": "Highland, Utah",
        "id_num": 23298,
        "population": 19974,
        "crime_rate": 23.05,
        "rental_rate": 1483.17,
        "walk_score": 31.93
        }
    ],
    [
        {
        "city_state": "Seymour, Indiana",
        "id_num": 8922,
        "population": 19991,
        "crime_rate": 52.6,
        "rental_rate": 1466.89,
        "walk_score": 39
        }
    ],
    [
        {
        "city_state": "Nogales, Arizona",
        "id_num": 2150,
        "population": 19960,
        "crime_rate": 32.6,
        "rental_rate": 1461.8,
        "walk_score": 34
        }
    ],
    [
        {
        "city_state": "Shelby, North Carolina",
        "id_num": 15596,
        "population": 19938,
        "crime_rate": 33.66,
        "rental_rate": 1461.4,
        "walk_score": 28
        }
    ],
    [
        {
        "city_state": "Columbia Heights, Minnesota",
        "id_num": 14479,
        "population": 20103,
        "crime_rate": 26.6,
        "rental_rate": 1482.9,
        "walk_score": 53
        }
    ],
    [
        {
        "city_state": "Fernley, Nevada",
        "id_num": 16575,
        "population": 20033,
        "crime_rate": 24.5,
        "rental_rate": 1594.7,
        "walk_score": 16
        }
    ],
    [
        {
        "city_state": "Jollyville, Texas",
        "id_num": 26108,
        "population": 20112,
        "crime_rate": 21.83,
        "rental_rate": 1481.18,
        "walk_score": 30.68
        }
    ],
    [
        {
        "city_state": "Lake Ronkonkoma, New York",
        "id_num": 18299,
        "population": 20039,
        "crime_rate": 22.9,
        "rental_rate": 1361.25,
        "walk_score": 41
        }
    ],
    [
        {
        "city_state": "Alamo, Texas",
        "id_num": 25382,
        "population": 20144,
        "crime_rate": 21.83,
        "rental_rate": 1481.18,
        "walk_score": 36
        }
    ],
    [
        {
        "city_state": "Glassboro, New Jersey",
        "id_num": 16942,
        "population": 19856,
        "crime_rate": 18.3,
        "rental_rate": 1466.89,
        "walk_score": 38
        }
    ]
    ]