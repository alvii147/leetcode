SELECT EmployeeTable.Name AS Employee FROM
(SELECT * FROM Employee
WHERE ManagerId IS NOT NULL) AS EmployeeTable
INNER JOIN
(SELECT Id, Name, Salary
FROM Employee) AS ManagerTable
ON EmployeeTable.ManagerId = ManagerTable.Id
WHERE EmployeeTable.Salary > ManagerTable.Salary;
