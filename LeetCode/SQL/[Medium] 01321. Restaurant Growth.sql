# MySQL
with Dist_C as(
    select visited_on, sum(amount) Amt
    from Customer
    group by visited_on
    order by 1)

select visited_on, amount, average_amount
from(
    select  visited_on, 
            sum(Amt) over (order by visited_on rows between 6 preceding and current row) amount,
            round(avg(Amt) over (order by visited_on rows between 6 preceding and current row),2) average_amount
    from Dist_C) A
where DATE_ADD(visited_on, INTERVAL -6 DAY) in (select visited_on from Dist_C)
order by 1



# 다른 풀이
with day_total as (
select 
    visited_on, 
    sum(amount) as amount
from customer
group by visited_on)

select a.visited_on, 
    ROUND(SUM(b.amount),2) as amount,
    ROUND(AVG(b.amount),2) as average_amount
    from day_total a , day_total b
   where datediff (a.visited_on,b.visited_on) between 0 and 6 
    group by a.visited_on
    having count(*) > 6
order by a.visited_on



#  PostgreSQL
with Day as(
    select distinct visited_on
    from Customer
    where visited_on not in (select visited_on from Customer group by visited_on order by 1 limit 6)
    order by 1)

select D.visited_on, 
      (select sum(amount) 
       from Customer 
       where visited_on between D.visited_on-6 and D.visited_on) amount,
      (select round(sum(amount)::numeric/7,2)
       from Customer 
       where visited_on between D.visited_on-6 and D.visited_on) average_amount      
from Day D