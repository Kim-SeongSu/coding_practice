# MySQL & PostgreSQL
with ids as (
    select requester_id id from RequestAccepted 
    union all
    select accepter_id id from RequestAccepted
)

select id, count(id) num
from ids
group by id
order by 2 desc
limit 1