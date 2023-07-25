from kafka import KafkaConsumer
import json
import multiprocessing
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from clickhouse_driver import Client
from login_clickhouse import HOST, USER, PASSWORD, DB_TABLE, TABLE


def consume_from_kafka(kafka_topic, kafka_bootstrap_severs ):
    spark = SparkSession.builder.config("spark.driver.extraClassPath" \
                                    ,"./clickhouse/clickhouse-native-jdbc-shaded-2.5.4.jar").getOrCreate()
    client = Client(host=HOST, user=USER, password=PASSWORD, database=DB_TABLE)
    consumer = KafkaConsumer(kafka_topic, bootstrap_servers= kafka_bootstrap_severs \
                             , value_deserializer=lambda v: json.loads(v.decode('utf-8')))
    for message in consumer:
        data = message.value
        query = "INSERT INTO {} FORMAT JSONEachRow".format(TABLE)
        client.execute(query, [data])

        print("Reading data from kafka topic and write to clickhouse done !!!")
    consumer.close()


if __name__ == "__main__":
    kafka_bootstrap_severs = "192.168.56.1:9092"
    kafka_topic = "trending_coin"

    process = multiprocessing.Process(target=consume_from_kafka, args= (kafka_topic, kafka_bootstrap_severs))
    process.start()
    process.join()
