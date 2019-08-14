# -*- coding: utf-8 -*-
import re
import warnings
from urllib.parse import urlparse

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.httpobj import urlparse_cached

class ConnpassSpider(CrawlSpider):
    name = 'connpass'
    allowed_domains = ['connpass.com']
    start_urls = [
        'https://connpass.com/explore/'
    ]

    def parse(self, response):
        for link in LinkExtractor(canonicalize=True, unique=True, allow='/event/\d+/.*').extract_links(response):
            if self.is_allowed(link.url):
                yield {
                    'from': response.url,
                    'to': link.url,
                }

        for link in LinkExtractor(canonicalize=True, unique=True, deny='/event/\d+/.*').extract_links(response):
            if self.is_allowed(link.url):
                yield response.follow(response.urljoin(link.url), callback=self.parse)

    def is_allowed(self, url):
        regex = re.compile(r'^(.*\.)?(%s)$' % '|'.join(self.allowed_domains))
        return bool(regex.search(urlparse(url).netloc))
