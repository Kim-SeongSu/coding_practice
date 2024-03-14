# MySQL
select user_id, concat(upper(left(name,1)),lower(substring(name,2))) name
from Users
order by 1



# PostgreSQL
select user_id, concat(upper(left(name,1)),lower(right(name,-1))) name
from Users
order by 1