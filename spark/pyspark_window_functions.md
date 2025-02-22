Yes! Here’s a list of commonly used **window functions** in PySpark, categorized by their functionality:

---

## **1. Ranking Functions** (Used for ranking rows within partitions)
| Function | Description |
|----------|------------|
| `rank()` | Assigns a **unique** rank to each row within a partition, with gaps for ties (1, 2, 2, 4). |
| `dense_rank()` | Similar to `rank()`, but without gaps (1, 2, 2, 3). |
| `row_number()` | Assigns a unique **sequential** number to each row within a partition (no ties). |
| `ntile(n)` | Splits rows into `n` equal groups and assigns a bucket number (e.g., quartiles). |

**Example:**
```python
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, dense_rank, row_number

window_spec = Window.partitionBy("region").orderBy(col("sales").desc())

df.withColumn("rank", rank().over(window_spec)).show()
```

---

## **2. Aggregate Functions** (Used for summarizing data within partitions)
| Function | Description |
|----------|------------|
| `max(col)` | Returns the **maximum** value in the partition. |
| `min(col)` | Returns the **minimum** value in the partition. |
| `avg(col)` | Computes the **average** value in the partition. |
| `sum(col)` | Computes the **sum** of values in the partition. |
| `count(col)` | Counts the number of rows in the partition. |

**Example:**
```python
from pyspark.sql.functions import max, min, avg

df.withColumn("max_sales", max("sales").over(Window.partitionBy("region"))).show()
```

---

## **3. Lag and Lead Functions** (Used for accessing previous or next row values)
| Function | Description |
|----------|------------|
| `lag(col, n, default)` | Returns the value from `n` rows **before** the current row in the partition. |
| `lead(col, n, default)` | Returns the value from `n` rows **after** the current row in the partition. |

**Example:**
```python
from pyspark.sql.functions import lag, lead

window_spec = Window.partitionBy("region").orderBy("sales")

df.withColumn("prev_sales", lag("sales", 1).over(window_spec)).show()
df.withColumn("next_sales", lead("sales", 1).over(window_spec)).show()
```

---

## **4. Cumulative/Aggregated Functions** (Useful for running totals)
| Function | Description |
|----------|------------|
| `cume_dist()` | Computes the **cumulative distribution** of values within the partition. |
| `percent_rank()` | Similar to `rank()`, but returns a value between 0 and 1. |
| `sum(col).over(window_spec.rowsBetween(start, end))` | Calculates **running totals**. |

**Example: Running Sum**
```python
window_spec = Window.partitionBy("region").orderBy("sales").rowsBetween(Window.unboundedPreceding, 0)

df.withColumn("running_total", sum("sales").over(window_spec)).show()
```

---

## **5. First and Last Functions** (Fetches the first/last value in a partition)
| Function | Description |
|----------|------------|
| `first(col)` | Returns the **first** value in the partition. |
| `last(col)` | Returns the **last** value in the partition. |

**Example:**
```python
from pyspark.sql.functions import first, last

window_spec = Window.partitionBy("region").orderBy("sales")

df.withColumn("first_sales", first("sales").over(window_spec)).show()
df.withColumn("last_sales", last("sales").over(window_spec)).show()
```

---

## **Key Takeaways:**
1. **Use `rank()` or `dense_rank()`** when ranking is needed.
2. **Use `max()`, `sum()`, `count()`** for partition-wise aggregations.
3. **Use `lag()` and `lead()`** for previous/next row comparisons.
4. **Use `first()` and `last()`** to fetch boundary values.
5. **Use cumulative functions** (`sum().over()`) for running totals.
