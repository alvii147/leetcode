SELECT
    stock_name,
    sum(net_price) AS capital_gain_loss
FROM (
    SELECT
        stock_name,
        operation,
        IF(operation = "Buy", -price, price) AS net_price
    FROM Stocks) AS net_price_table
GROUP BY stock_name;