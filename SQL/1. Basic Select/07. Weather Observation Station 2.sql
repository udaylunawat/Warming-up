-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-2/problem
-- # Score: 15
-- # LEARNED ROUND AND SUM


select 
round(sum(LAT_N), 2), round(sum(LONG_W), 2) 
from station