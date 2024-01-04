# FROM CSVFEED TEMPLATE
from scrapy.spiders import CSVFeedSpider


class CsvSpiderSpider(CSVFeedSpider):
    name = "csv_spider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]
    #headers = ["id", "name", "description", "image_link"]
    #delimiter = "\t"

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = {}
        #i["url"] = row["url"]
        #i["name"] = row["name"]
        #i["description"] = row["description"]
        return i
