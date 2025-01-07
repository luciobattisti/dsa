* https://leetcode.com/problems/rising-temperature/

```sql
SELECT id FROM (
    SELECT id, 
        recordDate, 
        temperature,
        temperature - LAG(temperature) OVER(
            ORDER BY recordDate 
        ) AS diff_temperature,
        UNIX_TIMESTAMP(recordDate) - LAG(UNIX_TIMESTAMP(recordDate)) OVER(
            ORDER BY UNIX_TIMESTAMP(recordDate) 
        ) AS diff_date
    FROM Weather
) AS a
WHERE diff_temperature > 0 AND diff_date = 86400
```