# MySQL & PostgreSQL
select customer_number 
from Orders
group by customer_number
order by count(1) desc limit 1





SELECT customer_number FROM Orders
GROUP BY customer_number
ORDER BY COUNT(customer_number) DESC LIMIT 1;