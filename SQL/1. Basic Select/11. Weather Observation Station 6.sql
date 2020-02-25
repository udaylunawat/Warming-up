-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-6/problem
-- # Score: 10
-- # Learned SUBSTRING and REGEX
-- # https://www.w3schools.com/sql/func_mysql_substring.asp

#Oracle
SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(City, '^[AEIOU]');


#MySQL
SELECT CITY from station where substring(city,1,1) in ('a','e','i','o','u')
