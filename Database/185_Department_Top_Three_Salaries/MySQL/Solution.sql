SELECT Department.Name AS Department, TopEmployees.Name AS Employee, TopEmployees.Salary FROM
(SELECT Employee.DepartmentId, Employee.Name, Employee.Salary FROM
(SELECT Salary, DepartmentId FROM
(SELECT DistinctSalariesA.Salary, DistinctSalariesB.DepartmentId, COUNT(DistinctSalariesB.Salary) AS DepartmentRank FROM
(SELECT * FROM Employee
GROUP BY Salary, DepartmentId) AS DistinctSalariesA,
(SELECT * FROM Employee
GROUP BY Salary, DepartmentId) AS DistinctSalariesB
WHERE DistinctSalariesA.Salary <= DistinctSalariesB.Salary AND DistinctSalariesA.DepartmentId = DistinctSalariesB.DepartmentId
GROUP BY DistinctSalariesA.Id, DistinctSalariesA.Salary) AS RankedSalaries
WHERE DepartmentRank <= 3) AS TopThreeSalaries
INNER JOIN Employee
ON Employee.Salary = TopThreeSalaries.Salary AND Employee.DepartmentId = TopThreeSalaries.DepartmentId)
AS TopEmployees
INNER JOIN Department
ON TopEmployees.DepartmentId = Department.Id
ORDER BY Department, Employee;