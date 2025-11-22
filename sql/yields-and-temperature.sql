WITH cte AS (
SELECT 
	`Area` AS Country,
    `Year`,
    AVG(Value) AS avg_yields
 FROM ton
WHERE Element = 'Yield'
 GROUP BY `Area`,`Year`
 )
 
SELECT 
	lt.Country,
    lt.Year,
    avg_yields,
    AVG(Value) AS temperatures_avg
 FROM landt lt
 JOIN cte c
	ON lt.Country = c.Country
    AND lt.year = c.year
	WHERE Element = "Temperature change"
GROUP BY `Year`, Country
