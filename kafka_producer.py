from kafka import KafkaProducer
from craw_trendingcoin import crawl_trending_coin

kafka_bootstrap_severs = "192.168.56.1:9092"
producer = KafkaProducer(bootstrap_servers= kafka_bootstrap_severs, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
kafka_topic = "trending_coin"


def maintask():
    data = crawl_trending_coin()
    for row in data:
        producer.send(kafka_topic, value=row)
    producer.close()
    return print("Sending coin data to kafka Successfully")
    

maintask()
