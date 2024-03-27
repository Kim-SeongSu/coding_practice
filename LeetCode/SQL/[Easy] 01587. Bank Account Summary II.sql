# MySQL
select U.NAME, sum(amount) BALANCE
from Transactions T
    join Users U
    on T.account = U.account
group by T.account having sum(amount) > 10000


# PostgreSQL
select NAME, sum(amount) BALANCE
from Transactions T
    join Users U
    on T.account = U.account
group by NAME, T.account having sum(amount) > 10000