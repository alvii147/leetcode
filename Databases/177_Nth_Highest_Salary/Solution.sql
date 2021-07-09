CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE nthHighestSalary INT;

DECLARE offset_val INT;
SET offset_val = N - 1;

SELECT IFNULL(
(SELECT DISTINCT Salary
FROM Employee ORDER BY Salary DESC
LIMIT 1 OFFSET offset_val),
NULL)
INTO nthHighestSalary;

RETURN (nthHighestSalary);
END