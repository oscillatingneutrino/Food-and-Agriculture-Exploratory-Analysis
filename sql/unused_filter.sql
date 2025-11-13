
WITH cte AS(
SELECT Item FROM prices
	WHERE Unit = 'SLC'
    AND Months = 'Annual Value'
GROUP BY Item
HAVING COUNT(DISTINCT Area) = 3
-- WHERE Unit NOT IN("")
)
SELECT 
		p.Domain,
		p.Area, 
		p.Element,
		p.Item,
		p.Year,
		p.Months,
		p.Unit, 
		p.Value
 FROM prices p
	JOIN cte c
		ON p.Item = c.Item
	WHERE Unit = 'SLC'
    AND Months = 'Annual Value'
        
