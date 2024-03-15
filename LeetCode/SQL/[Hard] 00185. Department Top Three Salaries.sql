# MySQL&  PostgreSQL
select D.name "Department", E.name "Employee", salary "Salary"
from (select *, dense_rank() over (partition by departmentId order by salary desc) R
      from Employee) E
    left join Department D
    on E.departmentId = D.id
where E.R < 4