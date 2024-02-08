SELECT B.unique_id, A.name
FROM EmployeeUNI B
    RIGHT JOIN Employees A
    ON A.id = B.id