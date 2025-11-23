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
	`Area` AS Country,
	t.`Year`,
    avg_yields,
	AVG(Value) AS emissions_avg
FROM totals t
 JOIN cte c
	ON t.Area = c.Country
    AND t.year = c.year
GROUP BY `Year`, Country
