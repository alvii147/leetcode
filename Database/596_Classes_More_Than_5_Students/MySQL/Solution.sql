SELECT class FROM
(SELECT COUNT(student) AS students_count, class
FROM (SELECT DISTINCT * FROM courses) AS DistinctCourses
GROUP BY class) AS StudentsCount
WHERE students_count >= 5;
