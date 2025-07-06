# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CryptoscraperPipeline:
    def process_item(self, item, spider):
        return item


class CryptoPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        field_name = adapter.field_names()

        for i in field_name:
            value = adapter.get(i)

            if isinstance(value, tuple):
                value = value[0]

            if isinstance(value, str):
                value = value.strip()
                adapter[i] = value

        supply_key = ["AvailableSupply", "TotalSupply"]

        for i in supply_key:
            value = adapter.get(i)

            if isinstance(value, tuple):
                value = value[0]

            if isinstance(value, str) and value != "N/A":
                value = int(value)
                adapter[i] = value

        float_key = ["Price", "MarketCap"]

        for i in float_key:
            value = adapter.get(i)

            if isinstance(value, tuple):
                value = value[0]

            if value in [" ", "", None]:
                value = "N/A"
                adapter[i] = value
                continue

            if isinstance(value, str) and value != "N/A":
                value = float(value)
                adapter[i] = value

        return item
