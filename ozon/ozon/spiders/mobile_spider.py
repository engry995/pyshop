import scrapy
from scrapy import Request


class MobileSpider(scrapy.Spider):

    name = 'mobile'
    allowed_domains = ['ozon.ru']
    start_urls = [
        'https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?sorting=rating',
        # "http://quotes.toscrape.com/",
    ]

    def parse(self, response, **kwargs):
        print('\n\nresponse!!!'*5)
