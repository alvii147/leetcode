SELECT Email FROM
(SELECT Email, COUNT(Email) AS EmailCount
FROM Person
GROUP BY Email) AS DuplicateEmails
WHERE EmailCount > 1;