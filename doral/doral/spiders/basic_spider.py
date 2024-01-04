# FROM BASIC TEMPLATE
import scrapy


class BasicSpiderSpider(scrapy.Spider):
    name = "basic_spider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
