* https://leetcode.com/problems/swap-salary

```sql
UPDATE Salary
SET sex = CASE 
        WHEN sex = 'f' THEN 'm'
        WHEN sex = 'm' THEN 'f'
    END
```