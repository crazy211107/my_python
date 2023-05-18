from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PySpark Test").getOrCreate()
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
result = rdd.collect()

print(result)
