SQL **window functions** are powerful tools that allow you to perform calculations across a set of table rows that are related to the current row, while retaining the individual row details. These functions are commonly used for tasks like ranking, running totals, moving averages, and other aggregate-like operations.

### Components of Window Functions

A typical SQL window function has the following components:

```sql
<function_name>() OVER (
    [PARTITION BY <column>]
    [ORDER BY <column>]
    [frame_clause]
)
```

1. **`<function_name>`**: The specific window function to use (e.g., `ROW_NUMBER`, `RANK`, `SUM`).
2. **`PARTITION BY`**: Divides the result set into groups (optional).
3. **`ORDER BY`**: Specifies the order of rows within each partition.
4. **`frame_clause`**: Defines the subset of rows for the calculation (e.g., `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`).

---

### Common Window Functions

#### 1. **Ranking Functions**

- `ROW_NUMBER()`: Assigns a unique number to each row within a partition, based on the specified order.
- `RANK()`: Similar to `ROW_NUMBER`, but rows with the same value in the `ORDER BY` column get the same rank, leaving gaps.
- `DENSE_RANK()`: Like `RANK()`, but without gaps in the ranking.

**Example:**
```sql
SELECT 
    employee_id, department_id, salary,
    ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_num,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank,
    DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rank
FROM employees;
```

#### Output:
| employee_id | department_id | salary | row_num | rank | dense_rank |
|-------------|---------------|--------|---------|------|------------|
| 1           | 101           | 1000   | 1       | 1    | 1          |
| 2           | 101           | 1000   | 2       | 1    | 1          |
| 3           | 101           | 900    | 3       | 3    | 2          |

---

#### 2. **Aggregate Functions**

- `SUM()`, `AVG()`, `COUNT()`, `MIN()`, `MAX()`: Perform aggregations over a specific window of rows.

**Example (Running Total):**
```sql
SELECT 
    employee_id, salary,
    SUM(salary) OVER (ORDER BY employee_id) AS running_total
FROM employees;
```

#### Output:
| employee_id | salary | running_total |
|-------------|--------|---------------|
| 1           | 500    | 500           |
| 2           | 700    | 1200          |
| 3           | 400    | 1600          |

---

#### 3. **Value Functions**

- `LAG(column, offset)`: Accesses a value in a previous row.
- `LEAD(column, offset)`: Accesses a value in a subsequent row.
- `FIRST_VALUE(column)`: Returns the first value in the window.
- `LAST_VALUE(column)`: Returns the last value in the window.

**Example (Difference Between Rows):**
```sql
SELECT 
    employee_id, salary,
    LAG(salary) OVER (ORDER BY employee_id) AS prev_salary,
    salary - LAG(salary) OVER (ORDER BY employee_id) AS salary_diff
FROM employees;
```

#### Output:
| employee_id | salary | prev_salary | salary_diff |
|-------------|--------|-------------|-------------|
| 1           | 500    | NULL        | NULL        |
| 2           | 700    | 500         | 200         |
| 3           | 400    | 700         | -300        |

---

#### 4. **NTILE Function**

- Divides rows into a specified number of groups and assigns a group number.

**Example (Quartiles):**
```sql
SELECT 
    employee_id, salary,
    NTILE(4) OVER (ORDER BY salary) AS quartile
FROM employees;
```

#### Output:
| employee_id | salary | quartile |
|-------------|--------|----------|
| 1           | 400    | 1        |
| 2           | 500    | 2        |
| 3           | 700    | 3        |
| 4           | 1000   | 4        |

---

### Frame Clauses

The **frame clause** defines the subset of rows within the partition to be included in the calculation.

- `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`: Includes all rows from the start of the partition to the current row.
- `ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING`: Includes one row before and one row after the current row.

**Example (Moving Average):**
```sql
SELECT 
    employee_id, salary,
    AVG(salary) OVER (ORDER BY employee_id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS moving_avg
FROM employees;
```

#### Output:
| employee_id | salary | moving_avg |
|-------------|--------|------------|
| 1           | 500    | 600        |
| 2           | 700    | 533.33     |
| 3           | 400    | 550        |

---

### Advantages of Window Functions

1. **Non-Aggregative Nature**: Unlike `GROUP BY`, window functions retain all rows while applying calculations.
2. **Flexible Calculations**: Easily compute running totals, rankings, and differences.
3. **Efficiency**: Optimized for large datasets with partitions and frame clauses.

---

### Key Use Cases

- **Ranking in Leaderboards**: Use `RANK()` or `DENSE_RANK()` to rank players or items.
- **Financial Calculations**: Use running totals, moving averages, or cumulative sums.
- **Comparative Analysis**: Use `LAG()` and `LEAD()` to compare rows for trends or differences.
- **Segmented Aggregates**: Use `PARTITION BY` to apply calculations within specific groups.

This flexibility and power make window functions a cornerstone of advanced SQL querying.