WITH
    NonSpringSales AS (
        SELECT P.product_id, P.product_name, S.sale_date < '2019-01-01' OR S.sale_date > '2019-03-31' AS non_spring
        FROM Product AS P
        INNER JOIN Sales AS S
        USING (product_id)
    ),
    NonSpringSalesSum AS (
        SELECT product_id, product_name, SUM(non_spring) AS non_spring_sum
        FROM NonSpringSales
        GROUP BY product_id
    )
SELECT product_id, product_name
FROM NonSpringSalesSum
WHERE non_spring_sum = 0;
