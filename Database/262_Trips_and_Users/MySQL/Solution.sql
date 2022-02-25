SELECT Request_at AS Day, ROUND(AVG(Status), 2) AS 'Cancellation Rate' FROM
(SELECT IF(t.Status = 'completed', 0, 1) AS Status, t.Request_at FROM Trips AS t
INNER JOIN Users AS c
ON t.Client_Id = c.Users_Id AND c.Banned = 'No' AND c.Role = 'client'
INNER JOIN Users AS d
ON t.Driver_Id = d.Users_Id AND d.Banned = 'No' AND d.Role = 'driver'
WHERE t.Request_at BETWEEN '2013-10-01' AND '2013-10-03')
AS ValidTrips
GROUP BY Request_at;
