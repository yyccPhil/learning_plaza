-- MySQL are case-insensitive! This is really shocking to me. Although I know that keywords are case-insensitive, even the parameters to be queried are case-insensitive!!

-- Revising the Select Query I
select *
from CITY
where COUNTRYCODE = 'USA' and POPULATION > 100000

------------------------------------------------------------------------------------

-- Revising the Select Query II
select NAME
from CITY
where COUNTRYCODE = 'USA' and POPULATION > 120000

------------------------------------------------------------------------------------

-- Weather Observation Station 3
select distinct CITY
from STATION
where ID % 2 = 0

------------------------------------------------------------------------------------

-- Weather Observation Station 6
select distinct CITY
from STATION
where left(CITY, 1) IN ('A', 'E', 'I', 'O', 'U')

------------------------------------------------------------------------------------

-- Weather Observation Station 7
select distinct CITY
from STATION
where right(CITY, 1) in ('a', 'e', 'i', 'o', 'u')

------------------------------------------------------------------------------------

-- Weather Observation Station 8
select distinct CITY
from STATION
where left(CITY, 1) in ('A', 'E', 'I', 'O', 'U')
    and right(CITY, 1) in ('a', 'e', 'i', 'o', 'u')

------------------------------------------------------------------------------------

-- Weather Observation Station 11
-- either do not start with vowels or do not end with vowels. (either... or... !!!)
select distinct CITY
from STATION
where right(CITY, 1) not in ('a', 'e', 'i', 'o', 'u')
    or left(CITY, 1) not in ('A', 'E', 'I', 'O', 'U')

------------------------------------------------------------------------------------

-- Revising Aggregations - The Count Function
select count(id)
from city
where population > 100000

------------------------------------------------------------------------------------

-- Revising Aggregations - The Sum Function
select sum(population)
from city
where district = 'California'

------------------------------------------------------------------------------------

-- Revising Aggregations - Averages
select avg(population)
from city
where district = 'California'

------------------------------------------------------------------------------------

-- Average Population
select round(avg(population))
from city

------------------------------------------------------------------------------------

-- Japan Population
select sum(population)
from city
where countrycode = 'JPN'

------------------------------------------------------------------------------------

-- Population Density Difference
select max(population) - min(population)
from city

------------------------------------------------------------------------------------

-- Weather Observation Station 2
SELECT ROUND(SUM(LAT_N), 2) AS lat, ROUND(SUM(LONG_W), 2) AS lon
FROM STATION

