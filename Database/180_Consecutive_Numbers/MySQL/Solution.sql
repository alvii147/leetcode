SELECT Num1 FROM
(SELECT s1.Num1 AS Num1, s1.Num2 AS Num2, s2.Num3 AS Num3 FROM
(SELECT l2.Id, l1.Num AS Num1, l2.Num AS Num2 FROM
Logs AS l1 INNER JOIN Logs AS l2
ON l1.Id = l2.Id + 1) AS s1
INNER JOIN
(SELECT l2.Id, l2.Num AS Num2, l3.Num AS Num3 FROM
Logs AS l2 INNER JOIN Logs AS l3
ON l2.id = l3.id + 1) AS s2
ON s1.Id = s2.Id) AS ThreeColumnsTable
WHERE Num1 = Num2 AND Num2 = Num3;
