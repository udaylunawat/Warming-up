-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-11/problem
-- # Score: 15

-- # Oracle
SELECT DISTINCT City FROM Station
WHERE REGEXP_LIKE(City, '^[^AEIOU]|[^aeiou]$');


-- # Immature regex MySQL
select distinct city from station where city not regexp '^[aeiou].*' or city not regexp '[aeiou]$';


-- # MySQL REGEX
select distinct city from station where city regexp '^[^aeiou]|[^aeiou]$'