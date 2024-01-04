# FROM CRAWL TEMPLATE
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JsonCrawlerSpider(CrawlSpider):
    name = "json_crawler"
    allowed_domains = ["www.cityofdoral.com"]
    start_urls = ["https://www.cityofdoral.com/_odata/discounts?=adx_organizationname"]

    rules = (
        Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),
        )

    def parse_item(self, response):
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item
