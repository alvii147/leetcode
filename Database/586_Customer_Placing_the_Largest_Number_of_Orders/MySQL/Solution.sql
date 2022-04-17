WITH
    OrdersCount AS (
        SELECT COUNT(*) AS orders_count, customer_number
        FROM Orders
        GROUP BY customer_number
    )
SELECT customer_number
FROM OrdersCount
WHERE orders_count = (
    SELECT MAX(orders_count)
    FROM OrdersCount
);
