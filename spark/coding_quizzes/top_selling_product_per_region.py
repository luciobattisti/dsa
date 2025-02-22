from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, avg, count, rank, dense_rank, sum as spark_sum
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("Test").getOrCreate()

data = [
    (1, "North", "Laptop", 1000),
    (2, "North", "Tablet", 800),
    (3, "North", "Laptop", 1200),
    (4, "South", "Phone", 500),
    (5, "South", "Laptop", 1500),
    (6, "South", "Phone", 1000),
    (7, "West", "Tablet", 700),
    (8, "West", "Tablet", 1200),
    (9, "West", "Laptop", 1100),
]
df = spark.createDataFrame(data, ["id", "region", "product", "sales"])

df.show()

region_product_groups = (
    df.groupby(col("region"), col("product"))
    .agg(spark_sum("sales").alias("total_sales"))
)
ranked_total_sales = (
    region_product_groups.withColumn(
        "rank",
        dense_rank().over(
            Window.partitionBy(col("region")).orderBy(col("total_sales").desc())
        )
    )
)

top_selling_products = (
    ranked_total_sales.filter(col("rank") == 1)
)

top_selling_products.show()


