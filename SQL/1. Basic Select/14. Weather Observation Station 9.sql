-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-9/problem
-- # Score: 10

-- # Oracle
SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(City, '^[^AEIOU]');

-- # MySQL
select distinct city from station where not city regexp "^[aeiou].*"