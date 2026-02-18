# Write your MySQL query statement below
SELECT M.name 
FROM Employee AS M
JOIN(
    SELECT managerId
    FROM Employee
    GROUP BY managerID 
    HAVING COUNT(id) >= 5
) AS Sub
ON M.id = Sub.managerID
