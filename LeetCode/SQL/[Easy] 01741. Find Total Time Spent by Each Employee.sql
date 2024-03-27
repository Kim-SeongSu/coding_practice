# MySQL
select event_day day, emp_id, sum(out_time - in_time) total_time 
from Employees 
group by 2, 1


# PostgreSQL
select event_day as day, emp_id, sum(out_time - in_time) total_time 
from Employees 
group by 2, 1