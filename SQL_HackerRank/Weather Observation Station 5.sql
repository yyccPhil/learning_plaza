select CITY, length(CITY)
from STATION
order by length(CITY), CITY
limit 1;
-- (cannot use union here in MySQL and need to use ';' instead of union)
select CITY, length(CITY)
from STATION
order by length(CITY) desc, CITY
limit 1;
