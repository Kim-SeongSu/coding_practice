# MySQL
delete A.*
from Person A, Person B
where A.email = B.email and A.id > B.id



# PostgreSQL
delete 
from Person
where id not in (select min(id) from Person group by email)