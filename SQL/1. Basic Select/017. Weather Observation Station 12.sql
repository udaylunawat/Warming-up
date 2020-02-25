-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-11/problem
-- # Score: 15

-- # Oracle
SELECT DISTINCT City
FROM Station
WHERE REGEXP_LIKE(City, '^[^AEIOU].*[^aeiou]$');

-- # MySQL
select distinct city from station where city not regexp '^[aeiou]|[aeiou]$' 

-- # MySQL
select distinct city from station where city regexp '^[^aeiou]|[^aeiou]$' 