-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-10/problem
-- # Score: 10

-- # Oracle
SELECT DISTINCT City
FROM Station
WHERE REGEXP_LIKE(City, '[^aeiou]$');

-- # MySQL
select distinct city from station where city not regexp '[aeiou]$'