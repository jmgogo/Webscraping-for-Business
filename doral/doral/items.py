# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BusinessItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # business info...        
    business_name: str = scrapy.Field()
    industry: str = scrapy.Field()
    offer: str = scrapy.Field()
    website: str = scrapy.Field()
    phone: set[str] = scrapy.Field()
    contact_name: str = scrapy.Field()
