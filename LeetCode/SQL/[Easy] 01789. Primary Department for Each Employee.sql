# MySQL  &  postgreSQL
select distinct U.employee_id, U.department_id
from(select employee_id, department_id
     from Employee
     group by employee_id having count(employee_id) = 1
     union all
     select employee_id, department_id 
     from Employee
     where primary_flag = 'Y') U
order by 1



select employee_id,department_id 
from Employee 
where primary_flag = 'Y' or employee_id in 
    (select employee_id 
     from Employee 
     group by employee_id
     having count(department_id) = 1)
