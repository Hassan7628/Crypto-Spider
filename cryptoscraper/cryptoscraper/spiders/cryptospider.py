import scrapy
import json
from cryptoscraper.items import CryptoItem


class CryptospiderSpider(scrapy.Spider):
    name = "cryptospider"
    allowed_domains = ["api.cryptorank.io"]
    start_urls = ["https://api.cryptorank.io/v0/coins/v2"]

    custom_settings = {"FEEDS": {"data.csv": {"format": "csv"}}}

    def parse(self, response):
        data = json.loads(response.text)
        item = CryptoItem()

        for coin in data["data"]:
            item["Url"] = response.url
            item["Name"] = coin["name"]

            if 'price' in coin:
                item["Price"] = coin["price"]["USD"]
            else:
                item['Price'] = "N/A"

            item["Symbol"] = coin["symbol"]
            item["Type"] = coin["type"]

            if coin.get("category") and isinstance(coin["category"], dict) and "key" in coin["category"]:
                item["Category"] = coin["category"]["key"]
            else:
                item["Category"] = "N/A"

            if 'marketCap' in coin:
                item["MarketCap"] = coin["marketCap"]
            else:
                item["MarketCap"] = "N/A"
            
            if 'volume24h' in coin:
                item["Volume24h"] = coin["volume24h"]
            else:
                item['Volume24h'] = "N/A"
            
            if "totalSupply" in coin:
                item["TotalSupply"] = coin["totalSupply"]
            else:
                item["TotalSupply"] = "N/A"

            if 'availableSupply' in coin:
                item["AvailableSupply"] = coin["availableSupply"]
            else:
                item["AvailableSupply"] = "N/A"

            yield item
