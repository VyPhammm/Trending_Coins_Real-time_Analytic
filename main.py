from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

from login_mysql import USER, PASSWORD, HOST, PORT, DB_NAME, URL, DRIVER

spark = SparkSession.builder \
    .config('spark.jars', "C:\\spark\\mysql-connector-java-8.0.30.jar") \
        .getOrCreate()



final_output.write.format("jdbc") \
                    .option("driver",DRIVER) \
                    .option("url", URL) \
                    .option("dbtable", "trending_coins") \
                    .mode("append") \
                    .option("user", USER) \
                    .option("password", PASSWORD) \
                    .save()