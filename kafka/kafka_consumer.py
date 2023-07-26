from kafka import KafkaConsumer
from datetime import datetime
import json
import multiprocessing
from clickhouse_driver import Client


def consume_from_kafka(kafka_topic, kafka_bootstrap_severs, host, port, user, password, db_name, table):
    client = Client(host=host, port= port, user=user, password= password, database= db_name)
    consumer = KafkaConsumer(kafka_topic, bootstrap_servers= kafka_bootstrap_severs \
                             , value_deserializer=lambda v: json.loads(v.decode('utf-8')))
    for message in consumer:
        data = message.value
        data['time'] = datetime.strptime(data['time'], '%Y-%m-%d %H:%M:%S')

        query = "INSERT INTO {} FORMAT JSONEachRow".format(table)
        
        client.execute(query, [data])

        print("Reading data from kafka topic and write to ClickHouse done !!!")
    consumer.close()


if __name__ == "__main__":
    kafka_bootstrap_severs = "192.168.56.1:9092"
    kafka_topic = "trending_coin"
    host= 'localhost'
    port= '9000'
    user= "default"
    password= "" 
    db_name= 'coin'
    table= 'trending_coin'

    process = multiprocessing.Process(target=consume_from_kafka, args= (kafka_topic, kafka_bootstrap_severs, host, port, user, password, db_name, table))
    process.start()
    process.join()
