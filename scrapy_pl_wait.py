import scrapy
from tutorial.items import QuoteItem
import asyncio
from scrapy_playwright.page import PageMethod
''' ScrapeOps tutorial '''

class QuotesPlaywrightPySpider(scrapy.Spider):
    name = 'quotes_playwright.py'
    
   

    def start_requests(self):
        url = "http://quotes.toscrape.com/js/"
        yield scrapy.Request(url, meta=dict(
            playwright =True,
            playwright_include_page =True,
            playwright_page_methods = [
                PageMethod('wait_for_selector', 'div.quote')
            ], #wait for selector to be fully loaded
            errback = self.errback
        )) 
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            quote_item = QuoteItem()
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').get()
            yield quote_item
    
    
    async def errback(self,failure):
        page = failure.request.meta["playwright_page"]
        await page.close()