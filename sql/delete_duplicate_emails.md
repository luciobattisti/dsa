* https://leetcode.com/problems/delete-duplicate-emails/description/

```sql
WITH MinIdTable AS (
    SELECT MIN(id) AS id
    FROM Person
    GROUP BY email
)

DELETE FROM Person
WHERE id NOT IN (SELECT id FROM MinIdTable);
```