# MySQL & PostgreSQL
select request_at "Day", round(avg(case when status = 'completed' then 0 else 1 end),2) "Cancellation Rate"
from Trips T
where T.client_id not in (select users_id from Users where banned = 'Yes') and
      T.driver_id not in (select users_id from Users where banned = 'Yes')
group by request_at having request_at between '2013-10-01' and '2013-10-03'