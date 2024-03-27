# MySQL & PostgreSQL
select D.name "Department", E.name "Employee", Salary
from Employee E
    left join Department D
    on E.departmentId = D.id
where (departmentId,salary ) in (select departmentId, max(salary) Salary from Employee group by 1 ) 