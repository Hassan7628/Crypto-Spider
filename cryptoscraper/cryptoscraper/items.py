# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CryptoscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CryptoItem(scrapy.Item):
    Url = scrapy.Field()
    Name = scrapy.Field()
    Price = scrapy.Field()
    Symbol = scrapy.Field()
    Type = scrapy.Field()
    Category = scrapy.Field()
    MarketCap = scrapy.Field()
    Volume24h = scrapy.Field()
    TotalSupply = scrapy.Field()
    AvailableSupply = scrapy.Field()