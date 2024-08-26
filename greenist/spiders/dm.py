from datetime import datetime
from json import loads
from typing import Iterable

import scrapy
from scrapy.http import Request, Response, HtmlResponse
from scrapy_playwright.page import PageMethod


# python3 -m dm_test.test_spiders.test_product
class DmSpider(scrapy.Spider):
    name = "dm_spider"
    allowed_domains = ["dm.de"]
    start_urls = ["https://www.dm.de/"]

    def parse(self, response: HtmlResponse):
        pass
