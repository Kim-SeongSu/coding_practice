select count(*) FISH_COUNT, month(TIME) MONTH
from FISH_INFO
group by 2
order by 2