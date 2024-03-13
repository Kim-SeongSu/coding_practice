# MySQL
(select U.name results
from Users U
    inner join (select user_id, count(rating) rated
                from MovieRating 
                group by user_id) MR
    on U.user_id = MR.user_id
order by rated desc, U.name
limit 1)
union
(select M.title results
from Movies M
    inner join (select movie_id, avg(rating) rate 
                from MovieRating 
                where created_at like '2020-02%'
                group by movie_id) MR
    on M.movie_id = MR.movie_id
order by rate desc, M.title 
limit 1)



# postgreSQL
(
select U.name results
from Users U
    inner join (select user_id, count(rating) rated
                from MovieRating 
                group by user_id) MR
    on U.user_id = MR.user_id
order by rated desc, U.name
limit 1
)
union all
(
select M.title results
from Movies M
    inner join (select movie_id, avg(rating) rate 
                from MovieRating 
                where created_at::text like '2020-02%'
                # where to_char(created_at, 'YYYY-MM') = '2020-02'
                group by movie_id) MR
    on M.movie_id = MR.movie_id
order by rate desc, M.title 
limit 1
)