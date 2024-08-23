from datetime import datetime

import scrapy
from scrapy.http import Request, Response, HtmlResponse


# python3 -m greenist_test.test_spiders.test_product
class ProductSpider(scrapy.Spider):
    name = "greenist_spider"
    allowed_domains = ["greenist.de"]
    start_urls = ["https://greenist.de"]

    def parse(self, response: HtmlResponse):
        breakpoint()

        date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        url = response.css('meta[property="og:url"]::attr(content)').get().strip()
        product_id = 3
        title = response.css('div.h1::text').get().strip()
        images = response.css('div.product--image-container source[type="image/webp"]::attr(srcset)').get().strip()
        price = f"{float(response.css('meta[itemprop="price"]::attr(content)').get().strip())*1.11:.2f}"

        yield {
            "date": date,
            "url": url,
            "source": "Greenist",
            "product_id": "",
            "existence": None,
            "title": title,
            "title_en": None,
            "description_en": None,
            "summary": None,
            "sku": None,
            "upc": None,
            "brand": "Janur",
        	"specifications": None,
            "categories": None,
            "images": images,
            "videos": None,
            "price": price,
            "available_qty": None,
            "options": None,
            "variants": None,
            "returnable": None,
            "reviews": None,
            "rating": None,
            "sold_count": None,
            "shipping_fee": None,
            "shipping_days_min": None,
            "shipping_days_max": None,
            "weight": None,
            "width": None,
            "height": None,
            "length": None
        }
