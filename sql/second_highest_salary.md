* https://leetcode.com/problems/second-highest-salary/

```sql
SELECT c.salary AS SecondHighestSalary FROM(
    SELECT COUNT(*), b.salary FROM (
        SELECT id, salary FROM
        (
            SELECT id, salary, 
            DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
            FROM Employee 
        ) AS a
        WHERE a.salary_rank = 2
    ) AS b
) AS c
```