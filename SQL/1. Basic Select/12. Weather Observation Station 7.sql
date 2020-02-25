-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-7/problem
-- # Score: 10
-- # Learned SUBSTR from end and REGEX at end
-- # https://www.w3schools.com/sql/func_mysql_substring.asp

-- # Oracle
SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(City, '[aeiou]$');

-- # MySQL
select distinct city from station where SUBSTR(CITY,LENGTH(CITY),1) IN ('a','e','i','o','u') ;

-- # If it is a positive number, this function extracts from the beginning of the string. 
-- # If it is a negative number, this function extracts from the end of the string