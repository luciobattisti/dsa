* https://leetcode.com/problems/duplicate-emails/submissions

```sql
SELECT email FROM

(
    SELECT email, COUNT(email) as email_count
    FROM Person 
    GROUP BY email
) AS a

WHERE email_count > 1
```