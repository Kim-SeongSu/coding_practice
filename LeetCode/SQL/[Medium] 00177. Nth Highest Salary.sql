# MySQL
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N=N-1;
  RETURN (select distinct salary 
          from Employee
          order by salary desc limit N,1);
END


# PostgreSQL
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (select distinct E.Salary 
                from Employee E
                order by E.Salary desc 
                limit case when N-1>=0 then 1 else 0 end
                offset case when n>0 then n-1 else 0 end);
END;
$$ LANGUAGE plpgsql;