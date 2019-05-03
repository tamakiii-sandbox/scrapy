import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for tags in response.css('body > div > div > div.col-md-4.tags-box > span'):
            yield {
                'text': tags.css('a::text').get(),
                'href': tags.css('a::attr("href")').get(),
            }
