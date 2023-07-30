# Trending_Coins_Real-time_Analytic
## Objective

This project focuses on building a real-time data analysis system of  top 30 trending cryptocurrencies that people are searching for on CoinMarketCap. The main goal is to store, analyze, and assist investors in making investment decisions. This system utilizes technologies such as Apache Kafka for data transmission from source to the system, ClickHouse for data storage, and Grafana for data visualization.
Specifically, the system continuously collects trending coin data data from data source (CoinMarketCap). This data is then
transmitted via Kafka to ClickHouse for storage and analysis. Then, Grafana is used to create charts and graphs to display the analyzed information about the trending coin data. For example, Market Cap and trading volume correlation chart.
- Tech stack: Apache Kafka, ClickHouse, Grafana, Docker, Python.

## Architecture

![coin](https://github.com/VyPhammm/Trending_Coins_Real-time_Analytics/assets/127418764/e1abb24a-24eb-4add-bbb0-037aa6cc4a27)

### Data in ClickHouse
- Sever

| Service               | URL                              | User/Password                                 |
| :-------------------: | :------------------------------: | :-------------------------------------------: |
| ClickHouse            | http://localhost:8123/           | default/''                                    |
| Grafana               | http://localhost:3000/           | admin/admin                                   |

- Data schema
```sh
.
root
 |-- time: datetime
 |-- no: int32 
 |-- name: string 
 |-- symbol: string 
 |-- price: float32 
 |-- _24h: float32 
 |-- _7d: integer
 |-- _30d: integer 
 |-- market_cap: int128 
 |-- volume_24h: int128 
```
### Visualizing Data with Grafana

<img width="929" alt="grafana_visualization" src="https://github.com/VyPhammm/Trending_Coins_Real-time_Analytics/assets/127418764/ebd1c4c3-cc63-4ec5-97a7-c3734ce85edf">

## Setup
### Pre-requisite
#### Kafka setup
- Read instructions in file ```kafka\Run kafka sever.txt```.
#### ClickHouse setup
- Install ClickHouse [Install](setup/clickhouse.md)
#### Grafana setup
- Install Grafana 
## Get Going!
- Setup Kafka service and start sending log data from website [Setup](setup/kafka.md)
- Setup Grafana for data visualization [Setup](setup/grafana.md)
