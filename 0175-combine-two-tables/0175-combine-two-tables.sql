# Write your MySQL query statement below
SELECT firstName, LastName, city, state 
FROM Person
LEFT JOIN Address 
    ON Person.personId = Address.personId;