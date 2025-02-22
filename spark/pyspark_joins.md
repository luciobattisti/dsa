### 🔗 **Quick Reference: PySpark Joins** 🔗

Joins in **PySpark** allow you to combine DataFrames based on common columns, similar to SQL joins.

---

## 🔹 **1. Types of Joins in PySpark**

| Join Type        | Description |
|-----------------|-------------|
| **Inner Join**   | Returns matching rows from both DataFrames. |
| **Left Join**    | Returns all rows from the left DataFrame and matching rows from the right. |
| **Right Join**   | Returns all rows from the right DataFrame and matching rows from the left. |
| **Full Outer Join** | Returns all rows from both DataFrames (fills unmatched with `NULL`). |
| **Left Semi Join** | Returns only rows from the left DataFrame that have a match in the right. |
| **Left Anti Join** | Returns rows from the left DataFrame that do **not** have a match in the right. |
| **Cross Join**   | Cartesian product (each row from one DF is combined with all rows from the other). |

---

## 🔹 **2. Syntax & Examples**

Assuming we have these DataFrames:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("JoinsExample").getOrCreate()

customers = [
    (1, "Alice"), (2, "Bob"), (3, "Charlie"), (4, "David")
]
orders = [
    (101, 1, 100), (102, 1, 200), (103, 2, 150), (104, 3, 50)
]

customers_df = spark.createDataFrame(customers, ["customer_id", "name"])
orders_df = spark.createDataFrame(orders, ["order_id", "customer_id", "amount"])
```

---

### ✅ **1. Inner Join (Default)**
- Returns rows where **customer_id** exists in both DataFrames.

```python
inner_join_df = customers_df.join(orders_df, "customer_id", "inner")
inner_join_df.show()
```
🔹 **Result:** Customers who placed orders.

---

### ✅ **2. Left Join**
- Returns all customers, even if they haven't placed an order.

```python
left_join_df = customers_df.join(orders_df, "customer_id", "left")
left_join_df.show()
```
🔹 **Result:** Unmatched rows from `orders_df` appear as `NULL`.

---

### ✅ **3. Right Join**
- Returns all orders, even if they don’t have a corresponding customer.

```python
right_join_df = customers_df.join(orders_df, "customer_id", "right")
right_join_df.show()
```

---

### ✅ **4. Full Outer Join**
- Returns all records from both DataFrames.

```python
full_outer_df = customers_df.join(orders_df, "customer_id", "outer")
full_outer_df.show()
```
🔹 **Result:** Fills `NULL` for unmatched values.

---

### ✅ **5. Left Semi Join**
- Returns only customers who **have at least one order**.

```python
left_semi_df = customers_df.join(orders_df, "customer_id", "left_semi")
left_semi_df.show()
```
🔹 **Result:** Filters `customers_df` to only include those who have a match in `orders_df`.

---

### ✅ **6. Left Anti Join**
- Returns customers **who never placed an order**.

```python
left_anti_df = customers_df.join(orders_df, "customer_id", "left_anti")
left_anti_df.show()
```
🔹 **Result:** Filters `customers_df` to exclude those present in `orders_df`.

---

### ✅ **7. Cross Join (Cartesian Product)**
- Matches **each row** from `customers_df` with **all rows** from `orders_df`.

```python
cross_join_df = customers_df.crossJoin(orders_df)
cross_join_df.show()
```
🔹 **Result:** The number of rows = `customers_df.count() * orders_df.count()`.

---

## 📌 **Performance Tips**
1. **Use Broadcast Joins for Small Datasets** 🏎️  
   ```python
   from pyspark.sql.functions import broadcast
   df = orders_df.join(broadcast(customers_df), "customer_id", "inner")
   ```
   ✅ **Boosts performance by reducing shuffling.**

2. **Avoid Cross Joins Unless Needed** ⚠️  
   - Can generate an extremely large dataset.

3. **Filter Early Before Joins** 🔥  
   ```python
   orders_df_filtered = orders_df.filter(col("amount") > 50)
   df = customers_df.join(orders_df_filtered, "customer_id", "inner")
   ```
   ✅ **Minimizes data before the join.**

---

## 🏆 **Final Summary**
| Join Type       | Keeps All from Left? | Keeps All from Right? | Keeps Only Matches? |
|----------------|---------------------|----------------------|----------------------|
| **Inner**      | ❌ No               | ❌ No                | ✅ Yes               |
| **Left**       | ✅ Yes              | ❌ No                | ✅ Yes               |
| **Right**      | ❌ No               | ✅ Yes               | ✅ Yes               |
| **Full Outer** | ✅ Yes              | ✅ Yes               | ✅ Yes               |
| **Left Semi**  | ✅ Yes (Filtered)   | ❌ No                | ✅ Yes               |
| **Left Anti**  | ✅ Yes (Filtered)   | ❌ No                | ❌ No                |
| **Cross Join** | ✅ Yes              | ✅ Yes               | ❌ No (All Combos)   |
