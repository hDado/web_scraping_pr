''' Demo of scrapy Playwright on quote JS rendered website '''

import scrapy
from tutorial.items import QuoteItem

class QuotesPlaywrightPySpider(scrapy.Spider):
    name = 'quotes_playwright.py'
    
   

    def start_requests(self):
        url = "http://quotes.toscrape.com/js/"
        yield scrapy.Request(url, meta={'playwright':True}) 
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            quote_item = QuoteItem()
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').get()
            yield quote_item
