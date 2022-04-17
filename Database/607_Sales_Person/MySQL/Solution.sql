SELECT name
FROM SalesPerson
WHERE name NOT IN (
    SELECT SP.name
    FROM Orders AS O
    INNER JOIN (
        SELECT com_id
        FROM Company
        WHERE name = 'RED'
    ) AS C
    USING (com_id)
    INNER JOIN SalesPerson AS SP
    USING (sales_id)
)
