# MySQL & PostgreSQL
select stock_name, sum(case operation when 'Buy' then -1*price else price end) capital_gain_loss
from Stocks
group by 1