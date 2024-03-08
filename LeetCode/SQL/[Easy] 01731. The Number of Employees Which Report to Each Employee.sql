# MySQL & PostgreSQL
select employee_id, name, B.reports_count, B.average_age 
from Employees A
    inner join (select reports_to id, count(reports_to) reports_count, round(avg(age)) average_age 
                 from Employees 
                 group by reports_to having reports_to is not null) B
    on A.employee_id = B.id
order by 1