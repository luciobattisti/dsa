from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("CustomerCategorization").getOrCreate()

customers_data = [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie"),
    (4, "David"),
    (5, "Eve")
]

orders_data = [
    (101, 1, 100),
    (102, 1, 200),
    (103, 2, 150),
    (104, 2, 50),
    (105, 3, 600)
]

customers_df = spark.createDataFrame(customers_data, ["id", "customer"])
orders_df = spark.createDataFrame(orders_data, ["id", "customer_id", "total_amount"])

customers_df.show()
orders_df.show()

one_order_df = (
    customers_df.join(orders_df, customers_df.id == orders_df.customer_id, "left_semi")
)

one_order_df.show()

