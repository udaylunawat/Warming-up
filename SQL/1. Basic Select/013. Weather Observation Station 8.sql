-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-8/problem
-- # Score: 15

-- # Proper REGEX (Oracle)
SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(City, '^[AEIOU].*[aeiou]$');

-- # MySQL
select DISTINCT CITY
from STATION
where SUBSTR(CITY, 1, 1) IN  ('a','e','i','o','u')
AND SUBSTR(CITY, LENGTH(CITY), 1) IN  ('a','e','i','o','u')


-- # Immature REGEX
select distinct city from station where CITY regexp'[aeiou]{1}$' and CITY regexp'^[aeiou].*'