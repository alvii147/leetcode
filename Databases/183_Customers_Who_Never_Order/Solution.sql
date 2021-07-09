SELECT C.Name as Customers FROM
Customers AS C
LEFT JOIN
Orders AS O
ON C.Id = O.CustomerId
WHERE O.CustomerId IS NULL;