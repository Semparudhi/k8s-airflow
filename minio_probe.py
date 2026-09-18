from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("minio-probe").getOrCreate()
df = spark.read.option("header", True).csv("s3a://spark-data/input/")
df.show()
spark.stop()