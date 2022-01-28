import scrapy
from pymongo import MongoClient
import json

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    #pymongo.MongoClient
    
    start_urls = ['https://www.zyte.com/blog/']
      

    def parse(self, response):


        for title in response.css('.oxy-post-title'):
            yield {
                'title': title.css('::text').get()
            } 

'''
        client = MongoClient('localhost', 27017)
        db = client['titles']
        collection_currency = db['title']

        with open('data.json') as f:


            file_data = json.load(f)

# if pymongo < 3.0, use insert()
#collection_currency.insert(file_data)
# if pymongo >= 3.0 use insert_one() for inserting one document
       # collection_currency.insert_one(file_data)
# if pymongo >= 3.0 use insert_many() for inserting many documents
        collection_currency.insert_many(file_data)

        client.close()   
      '''
        #for icerik in response.css('script[id=registrationPopupTemplate]'):
       #     yield {
      #          'baslik':icerik.css('div.buttons a::text').get()
     #       }
         

            #https://www.youtube.com/watch?v=Z2Gi1Irv0iw
            #https://www.youtube.com/watch?v=ve_0h4Y8nuI&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=1
            #https://www.youtube.com/watch?v=djfnjtYB2co
            