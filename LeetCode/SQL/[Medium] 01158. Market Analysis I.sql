# MySQL
select user_id buyer_id, join_date, ifnull(cnt,0) orders_in_2019
from Users U
    left join (select buyer_id, count(*) cnt 
               from Orders
               where year(order_date) = '2019'
               group by 1) O
    on U.user_id = O.buyer_id


# PostgreSQL
select user_id buyer_id, join_date, coalesce(cnt,0) orders_in_2019
from Users U
    left join (select buyer_id, count(*) cnt 
               from Orders
               where to_char(order_date,'yyyy') = '2019'
               group by 1) O
    on U.user_id = O.buyer_id