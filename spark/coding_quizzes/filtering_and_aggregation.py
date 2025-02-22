from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, avg

spark = SparkSession.builder.appName("Test").getOrCreate()
data = [
    (1, "Alice", 25, 50000),
    (2, "Bob", 30, 60000),
    (3, "Carol", 22, 52000),
    (4, "Dave", 45, 80000),
    (5, "Eve", 35, 72000)
]
df = spark.createDataFrame(data, ["id", "name", "age", "salary"])

df.show()


def calculate_salary_avg(df: DataFrame, age: int = 25) -> int:
    return (
        df.filter(col("age") > age)
        .agg(avg("salary"))
    ).collect()[0][0]


print(calculate_salary_avg(df))