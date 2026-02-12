# Write your MySQL query statement below
SELECT E.name AS Employee
FROM Employee AS E
JOIN Employee AS M
ON E.managerId = M.id
WHERE E.salary > M.salary