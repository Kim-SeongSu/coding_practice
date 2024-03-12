# MySQL
with 
L as(select "Low Salary" category, count(account_id) accounts_count 
      from Accounts where income <20000),
A as(select "Average Salary" category, count(account_id) accounts_count 
      from Accounts where income between 20000 and 50000),
H as(select "High Salary" category, count(account_id) accounts_count 
      from Accounts where income >50000)

select * from L
union all
select * from A
union all
select * from H



# postgreSQL
select 'Low Salary' category, count(*) accounts_count from Accounts where income <20000
union all
select 'Average Salary' category, count(*) accounts_count from Accounts where income between 20000 and 50000
union all
select 'High Salary' category, count(*) accounts_count from Accounts where income >50000