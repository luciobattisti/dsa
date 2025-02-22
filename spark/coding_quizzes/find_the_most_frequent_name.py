from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, avg, count, rank
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("Test").getOrCreate()

data = [
    (1, "Alice", 25),
    (2, "Bob", 30),
    (3, "Alice", 22),
    (4, "Charlie", 35),
    (5, "Bob", 40),
    (6, "Alice", 29)
]
df = spark.createDataFrame(data, ["id", "name", "age"])

df.show()

name_groups = df.groupby(col("name")).agg(count("*").alias("count"))
ranked_names = name_groups.withColumn("rank", rank().over(Window.partitionBy("name").orderBy(col("count").desc())))
most_frequent_name = ranked_names.filter(col("rank") == 1)
most_frequent_name.show()
