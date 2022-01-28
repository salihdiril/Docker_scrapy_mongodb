# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
from pymongo import MongoClient
import json


import pymongo

class EmirhanPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri='mongodb://localhost:27017',
            mongo_db='scrapydb'
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
'''
class EmirhanPipeline(object):

    def __init__(self):

        1==1 
       # self.conn=pymongo.MongoClient("localhost",27017)
        #db=self.conn["amazondb"]
        #self.collection=db["amazoncol"]

    def process_item(self, item, spider):
        client = MongoClient('localhost', 27017)
        db = client['titles']
        collection_currency = db['title']
        with open('data.json') as f:


            file_data = json.load(f)
        collection_currency.insert_one(file_data)

        client.close()
        #self.collection.insert(dict(item))
        return item
'''