from datetime import datetime
from re import findall

import scrapy
from scrapy.http import Request, Response, HtmlResponse


# python3 -m greenist_test.test_spiders.test_product
class VitalaboSpider(scrapy.Spider):
    name = "vitalabo_spider"
    allowed_domains = ["vitalabo.com"]
    start_urls = []

    def parse(self, response: HtmlResponse):
        breakpoint()
