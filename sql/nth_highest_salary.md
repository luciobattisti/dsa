* https://leetcode.com/problems/nth-highest-salary/description/?envType=problem-list-v2&envId=e97a9e5m

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT salary
      FROM (
        SELECT id, salary,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS salary_rank
        FROM Employee
      ) AS a
      WHERE a.salary_rank = N
      LIMIT 1
  );
END
```