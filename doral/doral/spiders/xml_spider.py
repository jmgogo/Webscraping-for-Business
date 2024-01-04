# FROM XMLFEED TEMPLATE
from scrapy.spiders import XMLFeedSpider


class XmlSpiderSpider(XMLFeedSpider):
    name = "xml_spider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]
    iterator = "iternodes"  # you can change this; see the docs
    itertag = "item"  # change it accordingly

    def parse_node(self, response, selector):
        item = {}
        #item["url"] = selector.select("url").get()
        #item["name"] = selector.select("name").get()
        #item["description"] = selector.select("description").get()
        return item
