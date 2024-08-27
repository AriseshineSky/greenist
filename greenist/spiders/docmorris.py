from datetime import datetime
from json import loads

import scrapy
from scrapy.http import Request, Response, HtmlResponse


# python3 -m docmorris_test.test_spiders.test_product
class DocMorrisSpider(scrapy.Spider):
    name = "docmorris_spider"
    allowed_domains = ["docmorris.de"]
    start_urls = ["https://www.docmorris.de/"]

    def parse(self, response: HtmlResponse):
        try:
            prod_info = loads(response.css('script#__NEXT_DATA__::text').get().strip())['props']['pageProps']['product']
            print(prod_info)
        except:
            return

        url = 'https://www.docmorris.de'+prod_info['url']
        product_id = prod_info['readableId']
        existence = prod_info['available']
        title = prod_info['name']

        # TODO
        description = None

        upc = prod_info['code']
        brand = prod_info['brand']
        categories = " > ".join([bc['name'] for bc in prod_info['breadcrumbs']])

        images = None
        if prod_info['images']:
            images = ";".join([])

        yield {
            "date": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            "url": url,
            "source": "DocMorris",
            "product_id": product_id,
            "existence": existence,
            "title": title,
            "title_en": None,
            "description": description,
            "summary": None,
            "sku": product_id,
            "upc": upc,
            "brand": brand,
            "specifications": None,
            "categories": categories,
            # "images": images,
            # "videos": videos,
            # "price": price,
            # "available_qty": available_qty,
            # "options": None,
            # "variants": None,
            "returnable": False,
            # "reviews": reviews,
            # "rating": rating,
            # "sold_count": None,
            # "shipping_fee": 5.49,
            # "shipping_days_min": 2,
            # "shipping_days_max": 3,
            # "weight": weight,
            # "width": None,
            # "height": None,
            # "length": length
        }
