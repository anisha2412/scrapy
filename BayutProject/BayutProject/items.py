# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BayutprojectItem(scrapy.Item):
    # define the fields for your item here like:
    property_id = scrapy.Field()
    purpose = scrapy.Field()
    type = scrapy.Field()
    added_on = scrapy.Field()
    furnishing = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    bed_bath_size = scrapy.Field()
    permit_no = scrapy.Field()
    agent_name = scrapy.Field()
    image_url = scrapy.Field()
    breadcrumbs = scrapy.Field()
    amenities = scrapy.Field()
    description = scrapy.Field()
    pass
