from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, avg, count, rank, dense_rank, sum as spark_sum, lag, row_number, coalesce, lit, min as spark_min, max as spark_max
from pyspark.sql.window import Window
from pyspark.sql.types import DateType, IntegerType

spark = SparkSession.builder.appName("Test").getOrCreate()

data = [
    (1, "Alice", "2024-02-01"),
    (2, "Alice", "2024-02-02"),
    (3, "Alice", "2024-02-04"),
    (4, "Alice", "2024-02-05"),
    (5, "Alice", "2024-02-06"),
    (6, "Bob", "2024-02-01"),
    (7, "Bob", "2024-02-03"),
    (8, "Bob", "2024-02-04"),
    (9, "Bob", "2024-02-05"),
    (10, "Bob", "2024-02-07")
]
df = spark.createDataFrame(data, ["id", "customer", "purchase_date"])

df.show()

datetime_df = (
    df.withColumn(
        "purchase_datetime", col("purchase_date").cast(DateType())
    )
)

start_date_df = (
    datetime_df.withColumn(
        "start_date",
        spark_min("purchase_datetime").over(
            Window.partitionBy("customer").orderBy("purchase_datetime")
        )
    )
)

date_diff_df = (
    start_date_df.withColumn(
        "date_diff",
        (col("purchase_datetime") - col("start_date")).cast(IntegerType())
    )
)

streak_id_df = (
    date_diff_df.withColumn(
        "streak_id",
        col("id") - col("date_diff")
    )
)

grouped_streak_id = (
    streak_id_df.groupby(col("customer"), col("streak_id")).agg(count("*").alias("count"))
)

max_streak_id = (
    grouped_streak_id.groupby("customer").agg(spark_max("count").alias("longest_streak"))
)

max_streak_id.show()





