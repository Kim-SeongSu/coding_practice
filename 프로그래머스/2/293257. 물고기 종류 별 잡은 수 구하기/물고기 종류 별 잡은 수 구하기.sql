select I.FISH_COUNT, N.FISH_NAME
from FISH_NAME_INFO N
    right join (
        select FISH_TYPE, count(*) FISH_COUNT
        from FISH_INFO  
        group by FISH_TYPE) I
    on N.FISH_TYPE = I.FISH_TYPE
order by 1 desc