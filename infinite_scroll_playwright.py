import scrapy
from tutorial.items import QuoteItem
import asyncio
from scrapy_playwright.page import PageMethod


class QuotesPlaywrightPySpider(scrapy.Spider):
    name = 'quotes_playwright.py'
    
   

    def start_requests(self):
        #url = "http://quotes.toscrape.com/js/"
        url = "http://quotes.toscrape.com/scroll"
        yield scrapy.Request(url, meta=dict(
            playwright =True,
            playwright_include_page =True,
            playwright_page_methods = [
                PageMethod('wait_for_selector', 'div.quote'),
                PageMethod('evaluate', "window.scrollBy(0, document.body.scrollHeight)"),
                PageMethod('wait_for_selector', 'div.quote:nth-child(11)'), #10 per page
            ], #wait for selector to be fully loaded
            errback = self.errback
        )) 
    
    async def parse(self, response):

        page = response.meta["playwright_page"]
        await page.close()

        for quote in response.css('div.quote'):
            quote_item = QuoteItem()
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').get()
            yield quote_item
        
        #Pagination    
        # next_page = response.css('.next>a ::attr(href)').get()
        # if next_page is not None:
        #     next_page_url = 'http://quotes.toscrape.com' + next_page
        #     yield scrapy.Request(next_page_url, meta=dict(
        #     playwright =True,
        #     playwright_include_page =True,
        #     playwright_page_methods = [
        #         PageMethod('wait_for_selector', 'div.quote')
        #     ], #wait for selector to be fully loaded
        #     errback = self.errback
        # )) 
    
    async def errback(self,failure):
        page = failure.request.meta["playwright_page"]
        await page.close()