# MySQL
select *
from Users U
where mail regexp '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$'



# PostgreSQL
select *
from Users U
where mail ~ '^[A-Za-z][A-Za-z0-9.\_\-]*@leetcode.com'