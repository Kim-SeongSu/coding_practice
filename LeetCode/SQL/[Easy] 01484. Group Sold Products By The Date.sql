# MySQL
select sell_date, count(distinct product) num_sold, group_concat(distinct product) products
from Activities
group by sell_date
order by 1



# PostgreSQL
select sell_date, count(distinct product) num_sold, string_agg(distinct product, ',') products
from Activities
group by sell_date
order by 1