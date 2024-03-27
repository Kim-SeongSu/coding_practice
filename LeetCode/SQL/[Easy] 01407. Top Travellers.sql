# MySQL & PostgreSQL
select name, coalesce(sum(distance),0) travelled_distance 
from Users U
    left join Rides R
    on R.user_id = U.id
group by U.id, name
order by 2 desc, 1