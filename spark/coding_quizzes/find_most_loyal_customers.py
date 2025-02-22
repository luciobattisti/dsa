from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, avg, count, rank, dense_rank, sum as spark_sum, lag, row_number, coalesce, lit, min as spark_min, max as spark_max
from pyspark.sql.window import Window
from pyspark.sql.types import DateType, IntegerType

spark = SparkSession.builder.appName("Test").getOrCreate()

customers_data = [
    (1, "Alice", "2023-01-15"),
    (2, "Bob", "2023-03-10"),
    (3, "Charlie", "2023-06-20"),
    (4, "David", "2023-07-05"),
    (5, "Eve", "2023-09-30")
]

orders_data = [
    (101, 1, "2023-02-01", 100),
    (102, 1, "2023-03-05", 200),
    (103, 1, "2023-04-10", 150),
    (104, 2, "2023-05-15", 80),
    (105, 2, "2023-06-20", 120),
    (106, 3, "2023-07-25", 50),
    (107, 3, "2023-08-30", 60),
    (108, 3, "2023-09-05", 70),
    (109, 3, "2023-10-10", 90),
    (110, 4, "2023-11-15", 200)
]

customers_df = spark.createDataFrame(customers_data, ["id", "customer", "purchase_date"])
orders_df = spark.createDataFrame(orders_data, ["id", "customer_id", "order_date", "total_amount"])

customers_df.show()
orders_df.show()

total_df = (
    orders_df.groupby("customer_id")
    .agg(
        count("*").alias("total_orders"),
        spark_sum("total_amount").alias("total_spending")
    )
)

aggregate_df = (
    customers_df.join(total_df, customers_df.id == total_df.customer_id, "inner")
)

aggregate_df = (
    aggregate_df.select(
        col("customer").alias("name"),
        col("total_orders"),
        col("total_spending")
    )
    .orderBy(col("total_spending").desc())
    .filter(col("total_orders") >= 3)
)

aggregate_df.show()



