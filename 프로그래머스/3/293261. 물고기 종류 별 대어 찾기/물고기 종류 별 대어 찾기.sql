select ID, FISH_NAME, LENGTH
from FISH_INFO O
    left join FISH_NAME_INFO N
    on O.FISH_TYPE = N.FISH_TYPE
where (O.FISH_TYPE, LENGTH) in (select FISH_TYPE, max(LENGTH)
                              from FISH_INFO
                              group by FISH_TYPE)
order by ID