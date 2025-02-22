### 🚀 **Quick Reference: Spark UDFs** 🚀

Spark supports different types of **User-Defined Functions (UDFs)** to apply custom logic to DataFrames. Here’s a quick overview:

---

## 🔹 **1. Standard UDF (`udf`)**
- Works **row-by-row** (slow for large datasets).
- Uses Python functions but has high serialization overhead.

### **Example**
```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Define UDF
def categorize(x):
    return "Low" if x < 200 else "Medium" if x < 500 else "High"

categorize_udf = udf(categorize, StringType())

# Apply UDF
df = df.withColumn("category", categorize_udf(df["total_spending"]))
```

✅ **Use case:** Simple operations that don’t need batch processing.

---

## 🔹 **2. Pandas UDF (`pandas_udf`)** (Vectorized UDF)
- **Fastest option** using **Apache Arrow** for vectorized execution.
- Works on **Pandas Series** instead of row-by-row execution.

### **Example**
```python
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import StringType
import pandas as pd

@pandas_udf(StringType())
def categorize_pandas(spending: pd.Series) -> pd.Series:
    return spending.apply(lambda x: "Low" if x < 200 else "Medium" if x < 500 else "High")

df = df.withColumn("category", categorize_pandas(df["total_spending"]))
```

✅ **Use case:** Computationally expensive operations needing batch processing.

---

## 🔹 **3. SQL UDF (`registerFunction`)**
- Used when defining UDFs inside **Spark SQL queries**.
- Can register **Python functions** for direct SQL use.

### **Example**
```python
spark.udf.register("categorizeSQL", categorize, StringType())

df.createOrReplaceTempView("customers")
spark.sql("SELECT customer, total_spending, categorizeSQL(total_spending) AS category FROM customers").show()
```

✅ **Use case:** When working with **SQL queries** in Spark.

---

## 🔹 **4. Scala/Java UDF (Performance Optimized)**
- Defined in **Scala/Java** for better performance.
- Avoids Python **serialization overhead**.
- **Only for JVM-based execution**.

### **Example (Scala)**
```scala
import org.apache.spark.sql.functions.udf
val categorizeUDF = udf((x: Int) => if (x < 200) "Low" else if (x < 500) "Medium" else "High")
df.withColumn("category", categorizeUDF($"total_spending"))
```

✅ **Use case:** When performance is critical and Spark is running in a **JVM-only environment**.

---

## 📌 **Which UDF Should You Use?**
| UDF Type      | Speed  | Best For                     | Notes |
|--------------|--------|-----------------------------|-------|
| `udf`       | 🐌 Slow | Simple, row-wise functions | High serialization overhead |
| `pandas_udf` | 🚀 Fast | Large datasets, batch ops  | Uses Apache Arrow |
| `SQL UDF`   | ⚡ Medium | SQL queries                 | Easily callable in SQL |
| `Scala/Java UDF` | ⚡ Fastest | Performance-critical tasks | Best for JVM execution |
