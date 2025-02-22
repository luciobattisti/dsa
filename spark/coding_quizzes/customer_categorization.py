from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, sum as spark_sum, col
import pandas as pd


# Define categorize customer
def categorize_customer(x: int)->str:
    if x < 200:
        return "Low Spender"
    elif x < 500:
        return "Medium Spender"
    else:
        return "High Spender"


# Initialize Spark session
spark = SparkSession.builder.appName("CustomerCategorization").getOrCreate()

# Sample data for customers
customers_data = [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie")
]

# Sample data for orders
orders_data = [
    (101, 1, "2023-02-01", 100),
    (102, 1, "2023-03-05", 200),
    (103, 2, "2023-04-10", 150),
    (104, 2, "2023-05-15", 50),
    (105, 3, "2023-06-20", 600)
]

# Creating DataFrames
customers_df = spark.createDataFrame(customers_data, ["id", "customer"])
orders_df = spark.createDataFrame(orders_data, ["id", "customer_id", "order_date", "total_amount"])

# Show DataFrames
customers_df.show()
orders_df.show()

total_spending_df = (
    orders_df.groupby("customer_id")
    .agg(spark_sum("total_amount").alias("total_spending"))
)

aggregate_df = (
    customers_df.join(total_spending_df, customers_df.id == total_spending_df.customer_id, "inner")
)

categorize_customer_udf = udf(categorize_customer, StringType())

category_df = (
    aggregate_df.withColumn(
        "category",
        categorize_customer_udf(aggregate_df["total_spending"])
    ).select(
        col("customer"),
        col("total_spending"),
        col("category")
    )
)

category_df.show()
