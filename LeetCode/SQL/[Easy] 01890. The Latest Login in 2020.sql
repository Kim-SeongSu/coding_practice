# MySQL
select user_id, max(time_stamp) last_stamp
from Logins
where year(time_stamp) = '2020'
group by user_id


# PostgreSQL
select user_id, max(time_stamp) last_stamp
from Logins
where TO_CHAR(time_stamp, 'yyyy') = '2020'
group by user_id