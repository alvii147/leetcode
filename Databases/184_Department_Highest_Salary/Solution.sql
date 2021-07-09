SELECT Department.Name AS Department, Employee, Salary FROM
(SELECT Employee.Name AS Employee, Employee.Salary, Employee.DepartmentId
FROM Employee
INNER JOIN
(SELECT max(Salary) AS Salary, DepartmentId
FROM Employee
GROUP BY DepartmentId) AS GroupedSalaryTable
ON Employee.Salary = GroupedSalaryTable.Salary
AND Employee.DepartmentId = GroupedSalaryTable.DepartmentId) AS MaxSalaryTable
INNER JOIN
Department
ON Department.Id = MaxSalaryTable.DepartmentId
ORDER BY Department.Name;