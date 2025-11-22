WITH cte AS (
SELECT
	COUNT(`Area`) AS twentyfour,
    Item
	
	FROM ton
    WHERE Element = "Yield"
GROUP BY Item
),
cte2 AS (
SELECT
	*
	FROM ton)

SELECT *
	FROM cte2 q
    JOIN cte p
		ON p.item = q.item
WHERE twentyfour = 24
ORDER BY q.item ASC


-- Alternatively, one can use a HAVING COUNT(DISTINCT country) = 3 instead of the method used in cte, but this method obtains complete data.
-- Following is the alternative mentioned:
/*
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
*/
