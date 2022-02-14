from gc import callbacks
import scrapy
from ..items import BayutprojectItem
class BayutSpiderSpider(scrapy.Spider):
    name = 'Bayut'
    allowed_domains = ['https://www.bayut.com/to-rent/property/dubai/']
    start_urls = ['https://www.bayut.com/property/details-5719330.html']

    def parse(self, response):
        items = BayutprojectItem()
        property_id = response.css('._812aa185::text\n').extract()
        purpose = response.css('._812aa185::text\n').extract()
        type = response.css('._812aa185::text').extract()
        added_on = response.css('._812aa185::text').extract()

        furnishing = response.css('._812aa185::text').extract()
        price = response.css('._105b8a67::text').extract()
        location = response.css('._1f0f1758::text').extract()
        bed_bath_size = response.css('.fc2d1086::text').extract()

        permit_no = response.css('.ff863316::text').extract()
        agent_name = response.css('._55e4cba0::text').extract()
        image_url = response.css('._6681ac2b::text').extract()
        breadcrumbs = response.css('._74ac503e::text').extract()
        amenities = response.css('._005a682a::text').extract()
        description = response.css('_2015cd68 d320ecf0::text').extract()

        items['property_id']= property_id
        items['price']= price
        items['type']=type
        items['added_on']= added_on

        items['furnishing']= furnishing
        items['purpose']= purpose
        items['location']=location
        items['bed_bath_size']= bed_bath_size
        items['permit_no']= permit_no
        items['agent_name']= agent_name
        items['image_url']=image_url
        items['breadcrumbs']= breadcrumbs
        items['amenities']= amenities
        items['description']= description
        
        
        yield items
            # pass

