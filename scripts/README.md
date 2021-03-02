## Table of contents of scripts

* [Crime](./crime)
* [Walkability](./walkabilty)
* [Liveability ](./liveablity)

## Crime

At first, our group wanted to try to obtain crime data by zip code level, but it was determined that was outside the scope of our project for the time that we had to develop our project. We were able to obtain data via the [FBI](https://ucr.fbi.gov/crime-in-the-u.s) for the years 2014-2019. Within each year’s worth of data, the only columns that were kept were the Violent Crime, Property Crime, and Population for each city. Crime rates are typically shown in crime rate per 100,000 (see below for an example):

>A crime rate is calculated by dividing the number of reported crimes by the total population.
>The result is then multiplied by 100,000. For example, in 2014 there were 48,650 robberies in California and the population was 38,499 378. This equals a robbery crime rate of 126.4 per 100,000.


## Walkability

Walkability scores were obtained from [here](https://www.walkscore.com/). Via the website, Walk Score measures the walkability of any address using a patented system. For each address, Walk Score analyzes hundreds of walking routes to nearby amenities. Points are awarded based on the distance to amenities in each category. Amenities within a 5-minute walk (.25 miles) are given maximum points. A decay function is used to give points to more distant amenities, with no points given after a 30-minute walk.

Walk Score also measures pedestrian friendliness by analyzing population density and road metrics such as block length and intersection density. Data sources include Google, Factual, Great Schools, Open Street Map, the U.S. Census, Localeze, and places added by the Walk Score user community.


## Liveability

The liveablitly score is calculated by using the rental, walkability , and crime scores. Each score was weigthed equally to make a score out of 100. A higher score would indicate a city has a "more favorable living conditions" liveablity. 