# MySQL
update Salary 
set sex = if(sex='f','m','f')

#PostgreSQL
update Salary 
set sex = case when sex = 'm' then 'f' else 'm' end   # set sex = case sex when 'm' then 'f' else 'm' end