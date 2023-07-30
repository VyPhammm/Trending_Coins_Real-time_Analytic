# Run Kafka sever
### Go to the directory of kafka
### Start zoo keeper
```.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties```
### Start kafka server
```.\bin\windows\kafka-server-start.bat .\config\server.properties```
### Create kafka topic - kafka topic name: "trending_coin"
```.\bin\windows\kafka-topics.bat --create --bootstrap-server 192.168.56.1:9092 --replication-factor 1 --partitions 1 --topic trending_coin```
### Crawl coin data to kafka topic through kafka producer
``` Run script "kafka/kafka_producer.py"```
### Read data from kafka topic and storage in Data LakeHouse: ClickHouse
``` Run script "kafka/kafka_consumer.py"```
