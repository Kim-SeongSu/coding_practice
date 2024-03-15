# MySQL
select product_name, unit
from Products P
    join (
        select product_id, sum(unit) unit
        from Orders
        where order_date like '2020-02%'
        group by product_id having unit > 99
        ) O
    on P.product_id = O.product_id


# PostgreSQL
select product_name, unit
from Products P
    join (
        select product_id, sum(unit) unit
        from Orders
        where to_char(order_date, 'YYYY-mm') = '2020-02'
        group by product_id having sum(unit) > 99
        ) O
    on P.product_id = O.product_id