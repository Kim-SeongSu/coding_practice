/*
# MySQL
SELECT E.name, B.bonus
FROM Employee E
    LEFT JOIN Bonus B
    ON E.empId = B.empId
WHERE COALESCE(B.bonus,'null') < 1000
*/

-- postgreSQL
SELECT E.name, B.bonus
FROM Employee E
    LEFT JOIN Bonus B
    ON E.empId = B.empId
WHERE COALESCE(B.bonus,0) < 1000