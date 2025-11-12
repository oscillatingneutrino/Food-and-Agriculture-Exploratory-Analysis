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
