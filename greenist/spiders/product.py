from datetime import datetime

import scrapy
from scrapy.http import Request, Response, HtmlResponse


# python3 -m greenist_test.test_spiders.test_product
class ProductSpider(scrapy.Spider):
    name = "greenist_spider"
    allowed_domains = ["greenist.de"]
    start_urls = ["https://greenist.de"]

    def parse(self, response: HtmlResponse):
        # breakpoint()

        date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        url = response.css('meta[property="og:url"]::attr(content)').get().strip()
        product_id = 3
        images = response.css('div.product--image-container source[type="image/webp"]::attr(srcset)').get().strip()

        existence = False
        exist_sel = response.css('meta[property="og:availability"]::attr(href)')
        if exist_sel and (exist_sel.get().strip() == 'instock'):
            existence = True

        title = response.css('div.h1::text').get().strip()

        brand = response.css('meta[property="product:brand"]::attr(content)').get().strip()

        cat_list = [cat.get().strip() for cat in response.css('span.breadcrumb--title::text')[1:]]
        categories = " > ".join(cat_list)

        price = None
        price_sel = response.css('meta[itemprop="price"]::attr(content)')
        if price_sel:
            existence = True
            price = round(float(price_sel.get().strip())*1.11, 2)

        yield {
            "date": date,
            "url": url,
            "source": "Greenist",
            "product_id": None,
            "existence": existence,
            "title": title,
            "title_en": None,
            "description_en": None,
            "summary": None,
            "sku": None,
            "upc": None,
            "brand": brand,
        	"specifications": None,
            "categories": categories,
            "images": images,
            "videos": None,
            "price": price,
            "available_qty": None,
            "options": None,
            "variants": None,
            "returnable": False,
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
