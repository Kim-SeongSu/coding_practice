# MySQL  &  postgreSQL
select X.person_name 
from (select * , sum(weight) over(order by turn) as Total_Weight from Queue) X
where Total_Weight <= 1000
order by X.turn desc
limit 1

