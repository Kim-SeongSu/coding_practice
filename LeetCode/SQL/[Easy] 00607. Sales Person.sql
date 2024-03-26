# MySQL & PostgreSQL
select S.name
from SalesPerson S
where sales_id not in (
    select sales_id 
    from Orders O
        join (select * from Company where name = 'RED') C
        on O.com_id = C.com_id)