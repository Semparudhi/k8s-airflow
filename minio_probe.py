import time
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("minio-probe").getOrCreate()
df = spark.read.option("header", True).csv("s3a://spark-data/input/")
print("SLEEPING")
time.sleep(300)
df.write.mode("overwrite").partitionBy("city").parquet("s3a://spark-data/output/by_city/")
print("ROWS WRITTEN:", df.count())
spark.stop()