SELECT * FROM (
    SELECT
        u.name,
        SUM(t.amount) AS balance
    FROM Users AS u
    INNER JOIN Transactions AS t
    ON u.account = t.account
    GROUP BY u.account
) AS BalanceTable
WHERE balance > 10000;