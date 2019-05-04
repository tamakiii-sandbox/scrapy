# -*- coding: utf-8 -*-
import scrapy


class ConnpassSpider(scrapy.Spider):
    name = 'connpass'
    allowed_domains = ['conpass.com']
    start_urls = ['http://conpass.com/']

    def parse(self, response):
        pass
