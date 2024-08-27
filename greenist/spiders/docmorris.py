from datetime import datetime
from json import loads
from math import ceil

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
        product_id = prod_info['productId']
        existence = prod_info['available']
        title = prod_info['name']

        # TODO
        description = None

        # https://squareup.com/us/en/the-bottom-line/operating-your-business/stock-keeping-unit#:~:text=SKU%20stands%20for%20%E2%80%9Cstock%20keeping,has%20a%20unique%20SKU%20number.
        sku = prod_info['readableId'] # SKU通常为8位

        upc = prod_info['code']
        brand = prod_info['brand']
        categories = " > ".join([bc['name'] for bc in prod_info['breadcrumbs']])

        images = None
        if prod_info['images']:
            images = ";".join([img['variants']['420']['formats']['webp']['resolutions']['2x']['url'] for img in prod_info['images']])

        price = round(prod_info['prices']['salesPrice']['value']*1.11, 2)

        available_qty = None
        if not existence:
            available_qty = 0
        
        reviews = prod_info['reviewCount'] if prod_info['reviewCount'] else 0
        rating = round(prod_info['rating'], 1) if (prod_info['rating'] is not None) else None
        shipping_fee = 0.00 if price >= 21.09 else 3.89 # 19欧元及以上免运费

        weight = None
        width = None
        height = None
        length = None

        menge, einheit = prod_info['packagingSize'].strip().lower().split()
        if (einheit == 'ml') or (einheit == 'g'):

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
            "sku": sku,
            "upc": upc,
            "brand": brand,
            "specifications": None,
            "categories": categories,
            "images": images,
            "videos": None,
            "price": price,
            "available_qty": available_qty,
            "options": None,
            "variants": None,
            "returnable": False,
            "reviews": reviews,
            "rating": rating,
            "sold_count": None,
            "shipping_fee": shipping_fee,
            "shipping_days_min": 0,
            "shipping_days_max": 1,
            "weight": weight,
            "width": width,
            "height": height,
            "length": length
        }
