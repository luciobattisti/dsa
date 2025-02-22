## PySpark Interview Questions

---

### **1. Optimizing PySpark Jobs**
To optimize PySpark jobs for better performance, you can use several techniques:
- **Partitioning**: Distribute data efficiently across worker nodes to reduce data shuffling.
- **Caching/Persisting**: Store intermediate results in memory (`df.cache()`, `df.persist()`) to avoid recomputation.
- **Broadcasting**: Use `broadcast()` to send small lookup tables to all nodes, reducing data transfer in joins.
- **Reducing Shuffle Operations**: Minimize operations like `groupBy()`, `join()`, and `distinct()` that require data movement.
- **Optimized File Formats**: Use **Parquet** over CSV/JSON for efficient storage and retrieval.

---

### **2. Accumulators and Broadcast Variables**
- **Accumulators**: Shared variables used to aggregate values across worker nodes (e.g., counting errors).
- **Broadcast Variables**: Used to distribute read-only data efficiently to all nodes (e.g., lookup tables).
- **Usage**:
  ```python
  from pyspark.sql import SparkSession
  from pyspark.sql.functions import broadcast
  
  spark = SparkSession.builder.appName("Example").getOrCreate()
  df_small = spark.read.csv("small.csv")
  df_large = spark.read.csv("large.csv")
  
  df_joined = df_large.join(broadcast(df_small), "id")
  ```

---

### **3. Data Serialization in PySpark**
PySpark supports:
- **Java serialization (default but slower)**
- **Kryo serialization (faster, optimized for large objects)**  
  ```python
  spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
  ```
Efficient serialization reduces garbage collection overhead and speeds up job execution.

---

### **4. PySpark Memory Management**
- **Executor Memory**: Split into storage (for caching) and execution (for computations).
- **Common issues**:
  - **Out-of-Memory (OOM) errors**: Due to large dataset shuffles.
  - **Data skew**: Some partitions containing more data than others.
  - **Fixes**: Increase memory (`spark.executor.memory`), repartition data, or use **spill to disk**.

---

### **5. Checkpointing in PySpark**
- **Checkpointing** saves an RDD or DataFrame to disk to break lineage, reducing memory pressure.
- Useful in **iterative algorithms** (e.g., ML models) where long dependency chains slow down execution.
  ```python
  df.checkpoint()
  ```

---

### **6. Handling Skewed Data**
- **Salting keys**: Add a random suffix to keys to distribute data more evenly.
- **Using `broadcast()` for small tables** in joins.
- **Repartitioning the dataset** before shuffle-heavy operations.

---

### **7. Role of DAG (Directed Acyclic Graph)**
- DAG represents the logical execution plan.
- Helps Spark schedule tasks efficiently by breaking jobs into stages.
- Example: `df.groupBy().agg()` creates a DAG with **shuffle and aggregation stages**.

---

### **8. Pitfalls in Joining Large Datasets**
- **Data Skew**: Some partitions contain too much data.
- **Broadcast joins** can be used for small tables.
- **Salting keys** helps avoid **skewed shuffle operations**.

---

### **9. Unit Testing in PySpark**
- Use `pytest` and `unittest` to test PySpark code:
  ```python
  from pyspark.sql import SparkSession
  import pytest
  
  @pytest.fixture
  def spark():
      return SparkSession.builder.master("local").appName("test").getOrCreate()

  def test_data_count(spark):
      df = spark.createDataFrame([(1, "A"), (2, "B")], ["id", "value"])
      assert df.count() == 2
  ```

---

### **10. Real-Time Data Processing**
- **Uses Structured Streaming** with **Kafka**, **Delta Lake**, or **Event Hubs**.
- Example:
  ```python
  df = spark.readStream.format("kafka").option("subscribe", "topic").load()
  ```

---

### **11. Schema Enforcement**
- Helps avoid **schema mismatches** and improve performance.
- Can be defined explicitly using `StructType`:
  ```python
  from pyspark.sql.types import StructType, IntegerType, StringType

  schema = StructType().add("id", IntegerType()).add("name", StringType())
  df = spark.read.schema(schema).json("data.json")
  ```

---

### **12. Tungsten Execution Engine**
- **Improves performance** through:
  - **Bytecode generation** for CPU optimization.
  - **Managed memory** instead of JVM heap.
  - **Vectorized execution** for fast computations.

---

### **13. Window Functions in PySpark**
- Used for **ranking, running totals, and moving averages**.
- Example:
  ```python
  from pyspark.sql.window import Window
  from pyspark.sql.functions import row_number
  
  window_spec = Window.partitionBy("department").orderBy("salary")
  df.withColumn("rank", row_number().over(window_spec))
  ```

---

### **14. Custom Partitioning**
- Used when default hash partitioning causes skew.
- Example:
  ```python
  df = df.repartition(10, "id")  # Partitioning by ID
  ```

---

### **15. Handling Null Values**
- **Drop nulls**: `df.dropna()`
- **Fill with default values**: `df.fillna({"column": "default"})`
- **Replace nulls with expressions**: `df.na.fill("unknown")`

---

### **16. Debugging PySpark Applications**
- Use `spark.debug.maxToStringFields` to see all fields in logs.
- Enable event logging:
  ```python
  spark.conf.set("spark.eventLog.enabled", "true")
  ```
- Use `explain()` to inspect the execution plan.

---

### **17. Best Practices for Efficient PySpark Code**
- **Use `.select()` instead of `*`**
- **Avoid using UDFs when possible** (they run in Python, not JVM)
- **Cache results only when necessary**

---

### **18. Monitoring and Tuning Performance**
- **Use Spark UI** (`localhost:4040`) to inspect DAGs.
- **Enable task metrics logging**.
- **Tune Spark parameters** (`spark.executor.memory`, `spark.sql.shuffle.partitions`).

---

### **19. Custom UDFs in PySpark**
- Use **Pandas UDFs** instead of normal UDFs for better performance:
  ```python
  from pyspark.sql.functions import pandas_udf
  import pandas as pd

  @pandas_udf("double")
  def multiply_by_two(s: pd.Series) -> pd.Series:
      return s * 2
  ```

---

### **20. Optimizing Memory Usage**
- **Use `persist(StorageLevel.MEMORY_AND_DISK)`** to avoid OOM errors.
- **Increase executor memory (`spark.executor.memory`)**.
- **Use efficient formats like Parquet**.

---

### **21. Tungsten Execution Engine (Again)**
- Optimizes memory usage with **off-heap storage** and **zero-copy serialization**.

---

### **22. Persistence Storage Levels**
- `MEMORY_ONLY`: Fastest but can cause OOM.
- `DISK_ONLY`: Slower but avoids OOM.
- `MEMORY_AND_DISK`: Good balance.

---

### **23. Identifying and Resolving Memory Bottlenecks**
- **Use `df.explain(True)`** to inspect execution plans.
- **Check Spark UI for shuffle spills**.
- **Increase shuffle partitions** if tasks are underutilized.

---
