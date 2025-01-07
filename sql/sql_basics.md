### Common SQL Operations with Examples

SQL (Structured Query Language) is a powerful language for interacting with relational databases. Here is a summary of the most common SQL operations, organized by category, with practical examples.

---

### 1. **Data Retrieval: `SELECT`**

**Purpose:** Retrieve data from a database.

**Basic Query:**
```sql
SELECT column1, column2 FROM table_name;
```

**Example:**
```sql
SELECT first_name, last_name FROM employees;
```

**Retrieve All Columns:**
```sql
SELECT * FROM employees;
```

**Filter Rows with `WHERE`:**
```sql
SELECT first_name, salary
FROM employees
WHERE salary > 50000;
```

---

### 2. **Sorting Data: `ORDER BY`**

**Purpose:** Sort results in ascending (`ASC`) or descending (`DESC`) order.

**Example:**
```sql
SELECT first_name, salary
FROM employees
ORDER BY salary DESC;
```

---

### 3. **Filtering Rows: `WHERE`, `LIKE`, `BETWEEN`, `IN`**

**Using `LIKE`:**
```sql
SELECT first_name
FROM employees
WHERE first_name LIKE 'A%'; -- Names starting with 'A'
```

**Using `BETWEEN`:**
```sql
SELECT first_name, salary
FROM employees
WHERE salary BETWEEN 40000 AND 60000;
```

**Using `IN`:**
```sql
SELECT first_name
FROM employees
WHERE department_id IN (1, 2, 3);
```

---

### 4. **Aggregation: `GROUP BY` and Aggregate Functions**

**Purpose:** Group rows based on column values and perform aggregate calculations like `SUM`, `AVG`, `COUNT`, etc.

**Example:**
```sql
SELECT department_id, AVG(salary) AS average_salary
FROM employees
GROUP BY department_id;
```

**Filter Groups with `HAVING`:**
```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;
```

---

### 5. **Joins**

**Purpose:** Combine rows from two or more tables based on a related column.

**Inner Join (Matching Rows Only):**
```sql
SELECT employees.first_name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;
```

**Left Join (All Rows from Left Table):**
```sql
SELECT employees.first_name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id;
```

**Cross Join (Cartesian Product):**
```sql
SELECT employees.first_name, departments.department_name
FROM employees
CROSS JOIN departments;
```

---

### 6. **Insert Data: `INSERT`**

**Purpose:** Add new rows to a table.

**Single Row:**
```sql
INSERT INTO employees (first_name, last_name, department_id, salary)
VALUES ('John', 'Doe', 2, 50000);
```

**Multiple Rows:**
```sql
INSERT INTO employees (first_name, last_name, department_id, salary)
VALUES 
    ('Alice', 'Smith', 1, 60000),
    ('Bob', 'Johnson', 3, 45000);
```

---

### 7. **Update Data: `UPDATE`**

**Purpose:** Modify existing rows in a table.

**Example:**
```sql
UPDATE employees
SET salary = salary * 1.10
WHERE department_id = 2;
```

---

### 8. **Delete Data: `DELETE`**

**Purpose:** Remove rows from a table.

**Example:**
```sql
DELETE FROM employees
WHERE salary < 40000;
```

**Delete All Rows:**
```sql
DELETE FROM employees; -- Removes all rows
```

---

### 9. **Limit Results: `LIMIT` (or `FETCH` in SQL:2011)**

**Purpose:** Restrict the number of rows returned.

**Example:**
```sql
SELECT first_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 10;
```

---

### 10. **Subqueries**

**Purpose:** Use a query inside another query.

**Example (Filter Using Subquery):**
```sql
SELECT first_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

---

### 11. **Creating Tables: `CREATE TABLE`**

**Purpose:** Define a new table.

**Example:**
```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10, 2)
);
```

---

### 12. **Altering Tables: `ALTER TABLE`**

**Add Column:**
```sql
ALTER TABLE employees
ADD hire_date DATE;
```

**Modify Column:**
```sql
ALTER TABLE employees
MODIFY salary DECIMAL(15, 2);
```

---

### 13. **Deleting Tables: `DROP TABLE`**

**Purpose:** Delete an entire table from the database.

**Example:**
```sql
DROP TABLE employees;
```

---

### 14. **Indexes**

**Purpose:** Improve query performance by indexing columns.

**Create Index:**
```sql
CREATE INDEX idx_salary ON employees(salary);
```

**Drop Index:**
```sql
DROP INDEX idx_salary ON employees;
```

---

### 15. **Transactions**

**Purpose:** Ensure data consistency with a series of SQL commands.

**Example:**
```sql
BEGIN TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

COMMIT; -- Apply changes
-- Or
ROLLBACK; -- Undo changes
```

---

These operations form the foundation of SQL usage, allowing you to retrieve, manipulate, and analyze data efficiently.