/*
# MySQL
SELECT A.name
FROM Employee A
    INNER JOIN Employee B
    ON A.id = B.managerId
GROUP BY B.managerId
HAVING count(B.managerId) > 4
*/

-- # postgreSQL
SELECT A.name
FROM Employee A
    INNER JOIN Employee B
    ON A.id = B.managerId
GROUP BY A.name, B.managerId
HAVING count(B.managerId) > 4