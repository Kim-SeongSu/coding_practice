with RECURSIVE CTE as(
    select ID, PARENT_ID, 1 G
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
        union all
    select E.ID, E.PARENT_ID, G+1
    from ECOLI_DATA E
        join CTE C
        on E.PARENT_ID = C.ID)

select COUNT(*) COUNT,G GENERATION
from CTE
where id not in (select distinct parent_id from CTE where  parent_id is not null)
group by 2
order by 2