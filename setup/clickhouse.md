# ClickHouse by Docker
###
``` docker pull yandex/clickhouse-server ```
###
``` docker run -d --name my_clickHouse --ulimit nofile=262144:262144  -p 8123:8123 -p 9000:9000 yandex/clickhouse-server:latest ```
