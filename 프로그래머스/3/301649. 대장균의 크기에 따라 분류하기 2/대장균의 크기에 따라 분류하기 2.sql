with temp as(select ID, row_number() over(order by SIZE_OF_COLONY desc) r, count(*) over() t
             from ECOLI_DATA)

select ID, case when r <= t*0.25 then 'CRITICAL'
                when r <= t*0.5 then 'HIGH'
                when r <= t*0.75 then 'MEDIUM'
                else 'LOW' end COLONY_NAME
from temp
order by 1