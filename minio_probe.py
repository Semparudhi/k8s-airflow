from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("minio-probe").getOrCreate()
df = spark.read.option("header", True).csv("s3a://spark-data/input/")
df.write.mode("overwrite").partitionBy("city").parquet("s3a://spark-data/output/by_city/")
print("ROWS WRITTEN:", df.count())
spark.stop()