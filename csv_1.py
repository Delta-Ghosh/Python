from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

flight_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("mode", "FAILFAST") \
    .load("s3://my-bucket/flight_data.csv")
flight_df.show(5)