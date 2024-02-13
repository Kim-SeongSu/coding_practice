# MySQL & postgreSQL
SELECT P.project_id, round(avg(E.experience_years),2) average_years
FROM Project P
    INNER JOIN Employee E
    ON P.employee_id  = E.employee_id
GROUP BY P.project_id