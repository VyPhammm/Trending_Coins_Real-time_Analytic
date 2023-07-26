from kafka import KafkaProducer
from craw_trendingcoin import crawl_trending_coin
import time
import json

kafka_bootstrap_severs = "192.168.56.1:9092"
producer = KafkaProducer(bootstrap_servers= kafka_bootstrap_severs, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
kafka_topic = "trending_coin"


def main_task():
    data = crawl_trending_coin()
    for row in data:
        producer.send(kafka_topic, value=row)
    return print("Sending data to kafka Successfully")


status = "ON"
while status == "ON":
    main_task()
    time.sleep(5)
producer.close()    

