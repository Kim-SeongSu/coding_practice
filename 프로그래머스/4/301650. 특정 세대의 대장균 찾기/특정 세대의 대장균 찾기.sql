select ID
from ECOLI_DATA B
where PARENT_ID in (select ID
                    from ECOLI_DATA B
                    where PARENT_ID in ( select ID
                                    from ECOLI_DATA 
                                    where PARENT_ID is null))
order by 1