select ID, ifnull(B.C,0) CHILD_COUNT
from ECOLI_DATA A
    left join (select PARENT_ID, count(PARENT_ID) C
          from ECOLI_DATA
          where  PARENT_ID is not null
          group by PARENT_ID) B
    on A.ID = B.PARENT_ID
order by 1