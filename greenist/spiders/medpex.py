from datetime import datetime
from json import loads

import scrapy
from scrapy.http import Request, Response, HtmlResponse


# python3 -m dm_test.test_spiders.test_product
class MedpexSpider(scrapy.Spider):
    name = "medpex_spider"
    allowed_domains = ["medpex.de"]
    start_urls = ["https://www.dm.de/"]

    def parse(self, response: HtmlResponse):
        # breakpoint()

        date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        url = response.css('meta[property="og:url"]::attr(content)').get().strip()
        

        yield {
            "date": date,
            "url": url,
            "source": "medpex",
            
        }
