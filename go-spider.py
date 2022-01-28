from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapy_mongodb.spiders.pageavailability import PageavailabilitySpider


process = CrawlerProcess(get_project_settings())
process.crawl(PageavailabilitySpider)
process.start()
