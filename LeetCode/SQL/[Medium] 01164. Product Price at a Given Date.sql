# MySQL  &  postgreSQL
select distinct A.product_id, COALESCE(price, 10) price
from Products A
    left join ( select product_id, new_price price
                from Products 
                where (product_id, change_date) in (select product_id, max(change_date)
                                                              from Products
                                                   	  where change_date < '2019-08-17'
                                                   	  group by product_id) ) B
    on A.product_id = B.product_id