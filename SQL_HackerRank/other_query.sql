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

------------------------------------------------------------------------------------

-- Top Earners
SELECT months * salary AS earnings, count(months * salary) AS num_earnings
FROM Employee
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1

------------------------------------------------------------------------------------

-- Weather Observation Station 13
SELECT truncate(sum(LAT_N), 4)
FROM STATION
WHERE LAT_N < 137.2345 AND LAT_N > 38.788

------------------------------------------------------------------------------------

-- Weather Observation Station 14
SELECT truncate(LAT_N, 4)
FROM STATION
WHERE LAT_N < 137.2345
ORDER BY LAT_N DESC
LIMIT 1

------------------------------------------------------------------------------------

-- Weather Observation Station 15
SELECT round(LONG_W, 4)
FROM STATION
WHERE LAT_N = (
    SELECT max(LAT_N)
    FROM STATION
    WHERE LAT_N < 137.2345
)

------------------------------------------------------------------------------------

-- Weather Observation Station 16
SELECT round(min(LAT_N), 4)
FROM STATION
WHERE LAT_N > 38.778

------------------------------------------------------------------------------------

-- Weather Observation Station 17
SELECT round(LONG_W, 4)
FROM STATION
WHERE LAT_N = (
    SELECT min(LAT_N)
    FROM STATION
    WHERE LAT_N > 38.778
)

------------------------------------------------------------------------------------

-- Weather Observation Station 18
SELECT round(
        (SELECT max(LAT_N) FROM STATION) - (SELECT min(LAT_N) FROM STATION) +
        (SELECT max(LONG_W) FROM STATION) - (SELECT min(LONG_W) FROM STATION)
    , 4)
    

------------------------------------------------------------------------------------

-- Weather Observation Station 19
SELECT round(SQRT(
        POW(((SELECT max(LAT_N) FROM STATION) - (SELECT min(LAT_N) FROM STATION)), 2) + POW(((SELECT max(LONG_W) FROM STATION) - (SELECT min(LONG_W) FROM STATION)), 2)
    ), 4)
    
------------------------------------------------------------------------------------

-- Population Census
SELECT sum(CITY.POPULATION)
FROM CITY
LEFT JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.CONTINENT = 'Asia'

------------------------------------------------------------------------------------

-- African Cities
SELECT CITY.NAME
FROM CITY
LEFT JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.CONTINENT = 'Africa'

