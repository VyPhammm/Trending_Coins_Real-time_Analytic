import requests
from bs4 import BeautifulSoup
from datetime import datetime

result = requests.get('https://coinmarketcap.com/trending-cryptocurrencies/')
content = result.text
soup = BeautifulSoup(content, "html")

def convert_float(value):
    try:
        if '--' in value:
            return 0  
        else:
            return float(value)
    except ValueError:
        return 0
    
def convert_int(value):
    try:
        if '--' in value:
            return 0  
        else:
            return int(value)
    except ValueError:
        return 0
    
def replace_starting_with_zero(input_str):
    if input_str.startswith("0.0.."):
        return 0.000000001
    else:
        return float(input_str)
    
def crawl_trending_coin():
    trending_coin = []
    list_coin = soup.find("tbody").find_all("tr")
    for coin in list_coin :
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        name = coin.find_all("td")[2].find_all('div')[1].find('p').get_text()
        symbol = coin.find_all("td")[2].find_all('div')[2].find('p').get_text()
        price = replace_starting_with_zero(coin.find_all("td")[3].get_text().replace(",", "").replace("$", ""))
        h24h =  convert_float(coin.find_all("td")[4].find_all('span')[0].get_text().split('%')[0])
        ud_24h = coin.find_all("td")[4].find_all('span')[1].attrs.get('class')[0].split('-')[2]
        d7d = convert_float(coin.find_all("td")[5].find_all('span')[0].get_text().split('%')[0])
        ud_7d = coin.find_all("td")[5].find_all('span')[1].attrs.get('class')[0].split('-')[2]
        d30d = convert_float(coin.find_all("td")[6].find_all('span')[0].get_text().split('%')[0])
        ud_30d = coin.find_all("td")[6].find_all('span')[1].attrs.get('class')[0].split('-')[2]
        market_cap = convert_int(coin.find_all("td")[7].get_text().replace("$", "").replace(",", ""))
        vol24h = convert_int(coin.find_all("td")[8].get_text().replace("$", "").replace(",", ""))
        if ud_24h == "down":
            h24h = h24h * (-1)
        if ud_7d == "down":
            d7d = d7d* (-1)
        if ud_30d == "down":
            d30d = d30d* (-1)
        coin_info = {"time": time, "no":(list_coin.index(coin)+1), "name":name, "symbol":symbol,"price":price, "_24h":h24h, "_7d":d7d \
                    ,"_30d":d30d, "market_cap": market_cap, "volume_24h": vol24h}
        trending_coin.append(coin_info)
    return trending_coin
