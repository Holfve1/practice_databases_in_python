## 
"""
as a ferquent traveler
i want to organise the countries i have been to
i want to keep a list of countries

as a ferquent traveler
i want to keep a track of the cities i have been to
keep a list of the cities and what country they are in


"""
nouns
countries, cities 

| record   | properties |
-------------------------
| counties | country    |
| cities   | city       |

1. name of the first table will be: countries

    column name will be: country

2. name of the second tabel will be: cities

    column name will be: city

3. column types

Table: counties
id: SERIAL
country:: text

Table: cities
id: SERIAL
city: text

4. tables relationship

country can have many cities - one to many

5. write the SQL

CREATE TABLE countries (
id SERIAL PRIMARY KEY,
country text,
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city text
    country_id int,
)