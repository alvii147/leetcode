DELETE p FROM
Person AS p INNER JOIN
(SELECT min(Id) AS Id, Email
FROM Person
GROUP BY Email
ORDER BY min(Id))
AS DistinctPerson
ON p.Email = DistinctPerson.Email
AND p.Id <> DistinctPerson.Id;