from typing import Any
import scrapy
from scrapy.http import Response

start_path = '/find-a-church'
base_url = 'https://www.vancouver.anglican.ca'

class Parishes(scrapy.Spider):
    name = 'parishes'
    start_urls = [base_url + start_path]

    def parse_ads(self, response):

        for ads in response.css('div.relative.d-flex.flex-column.flex-grow-1'):

            this_url = base_url + ads.css('a.d-block.flex-grow-1').attrib['href'],

            yield{
               'www': this_url, 
                'name': ads.css('h2.mt-1.mb-1.h3::text').get().replace('\n',''),
                'parishes' : scrapy.Response(this_url,callback = self.parse_parishes),
            }
            

    def parse_parishes(self, response):

            for pars in response.css('div.relative.d-flex.flex-column.flex-grow-1'):
                yield{
                    'www': base_url + pars.css('a.d-block.flex-grow-1').attrib['href'], 
                    'name': pars.css('h2.mt-1.mb-1.h3::text').get().replace('\n',''),
                }