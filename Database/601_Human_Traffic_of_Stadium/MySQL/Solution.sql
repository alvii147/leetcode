SELECT DISTINCT stadium.* FROM stadium INNER JOIN
(SELECT a.id AS a_id, b.id AS b_id, c.id AS c_id
FROM stadium AS a
INNER JOIN stadium as b
INNER JOIN stadium as c
ON a.id = b.id - 1 AND b.id = c.id - 1
WHERE a.people >= 100 AND b.people >= 100 AND c.people >= 100)
AS over_100_table
ON stadium.id = over_100_table.a_id
OR stadium.id = over_100_table.b_id
OR stadium.id = over_100_table.c_id;
