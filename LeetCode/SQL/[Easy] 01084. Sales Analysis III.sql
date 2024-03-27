# MySQL & PostgreSQL
select S.product_id, product_name
from(
    select product_id
    from Sales
    group by 1 having min(sale_date) between '2019-01-01' and '2019-03-31'
                    and max(sale_date) between '2019-01-01' and '2019-03-31'
) S
    left join Product P
    on S.product_id = P.product_id