import scrapy


class ProductSpider(scrapy.Spider):
    name = "greenist_spider"
    allowed_domains = ["greenist.de"]
    start_urls = ["https://greenist.de"]

    def parse(self, response):
        pass
