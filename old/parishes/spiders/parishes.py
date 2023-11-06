from typing import Any
import scrapy
from scrapy.http import Response

start_path = '/find-a-church'
base_url = 'https://www.vancouver.anglican.ca'

class Parishes(scrapy.Spider):
    name = 'parishes'
    start_urls = [base_url + start_path]

    def parse(self, response):

        for ads in response.css('div.relative.d-flex.flex-column.flex-grow-1'):
            
            this_url = base_url + ads.css('a.d-block.flex-grow-1').attrib['href']
            yield{
                'www': this_url, 
                'name': ads.css('h2.mt-1.mb-1.h3::text').get().replace('\n',''),
            }
            if this_url is not None:
                yield scrapy.Request(response.urljoin(this_url))           