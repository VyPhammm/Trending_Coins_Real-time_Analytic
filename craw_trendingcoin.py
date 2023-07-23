import requests
from bs4 import BeautifulSoup
from datetime import datetime

result = requests.get('https://coinmarketcap.com/trending-cryptocurrencies/')
content = result.text
soup = BeautifulSoup(content, "html")

def crawl_trending_coin():
    trending_coin = []
    list_coin = soup.find("tbody").find_all("tr")
    for coin in list_coin :
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        name = coin.find_all("td")[2].find_all('div')[1].find('p').get_text()
        symbol = coin.find_all("td")[2].find_all('div')[2].find('p').get_text()
        price = coin.find_all("td")[3].get_text()
        h24h =  coin.find_all("td")[4].find_all('span')[0].get_text()
        ud_24h = coin.find_all("td")[4].find_all('span')[1].attrs.get('class')[0].split('-')[2]
        d7d = coin.find_all("td")[5].find_all('span')[0].get_text()
        ud_7d = coin.find_all("td")[5].find_all('span')[1].attrs.get('class')[0].split('-')[2]
        d30d = coin.find_all("td")[6].find_all('span')[0].get_text()
        ud_30d = coin.find_all("td")[6].find_all('span')[1].attrs.get('class')[0].split('-')[2]
        market_cap = int(coin.find_all("td")[7].get_text().replace("$", "").replace(",", ""))
        vol24h = int(coin.find_all("td")[8].get_text().replace("$", "").replace(",", ""))
        if ud_24h == "down":
            h24h = float(h24h.split('%')[0])* (-1)
        if ud_7d == "down":
            d7d = float(d7d.split('%')[0])* (-1)
        if ud_30d == "down":
            d30d = float(d30d.split('%')[0])* (-1)
        coin_info = {"No":list_coin.index(coin), "Name":name, "Symbol":symbol,"Price":price, "24h_%":h24h, "7d_%":d7d \
                    ,"30d_%":d30d, "Market_cap": market_cap, "Volume_24h": vol24h, "Time": time}
        trending_coin.append(coin_info)
    return trending_coin

crawl_trending_coin()
