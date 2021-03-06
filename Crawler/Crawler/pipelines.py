# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json


class CrawlerPipeline:
    def __init__(self):
        self.file = open('SFO Departing Flights.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = "\n" + json.dumps(dict(item), ensure_ascii=False) + ","
        self.file.write(line)
        return item

    def open_spider(self, spider):
        self.file.write('{"SFO Departing Flights":[')

    def close_spider(self, spider):
        # The following part is to remove the comma at the end of the last line of flights
        current_file_pointer_position = self.file.tell()
        self.file.close()
        self.file = open('SFO Departing Flights.json', 'r', encoding='utf-8')
        self.file.seek(current_file_pointer_position - 1)
        the_last_character = self.file.readline()
        self.file.close()
        if the_last_character == ',':
            self.file = open('SFO Departing Flights.json', 'a', encoding='utf-8')
            self.file.seek(current_file_pointer_position - 1)
            self.file.truncate()
            self.file.close()

        self.file = open('SFO Departing Flights.json', 'a', encoding='utf-8')
        self.file.write('\n]}')
        self.file.close()
