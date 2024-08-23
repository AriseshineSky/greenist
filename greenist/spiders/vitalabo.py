from datetime import datetime
from json import loads
from re import findall

import scrapy
from scrapy.http import Request, Response, HtmlResponse


# python3 -m vitalabo_test.test_spiders.test_product
class VitalaboSpider(scrapy.Spider):
    name = "vitalabo_spider"
    allowed_domains = ["vitalabo.com"]
    start_urls = ["https://www.vitalabo.com/"]

    def parse(self, response: HtmlResponse):
        # breakpoint()

        date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        url = response.css('meta[property="og:url"]::attr(content)').get().strip()

        try:
            prod_json = None
            jsons = response.css('script[type="application/ld+json"]')
            for j in jsons:
                cont = j.css('::text').get().strip()
                if ('"@type"' in cont) and ('"Product"' in cont):
                    prod_json = loads(cont)
        except:
            return

        product_id = prod_json['sku'] # 网页上“Item no.
        
        existence = False
        if 'instock' in prod_json['offers']['availability'].lower():
            existence = True

        title = prod_json['name']

        # 待完成：description_en
        descriptions = None

        upc = prod_json['gtin13']
        brand = prod_json['brand']['name']

        cat_sel = response.css('ul#js-breadcrumbs a')[1:]
        categories = " > ".join([cat.css("::text").get().strip() for cat in cat_sel])

        img_sel = response.css('div.bigslider img.product__image')
        images = ";".join([img.css("::src").get().strip().replace('256x256.jpg', '768x768.jpg') for img in img_sel])
        price = round(float(prod_json['offers']['price'])*1.11, 2)

        shipping_fee = round(prod_json['offers']['shippingDetails']['shippingRate']['value']*1.11, 2)
        

        yield {
            "date": date,
            "url": url,
            "source": "Greenist",
            "product_id": product_id,
            "existence": existence,
            "title": title,
            "title_en": title,
            "description_en": descriptions,
            "summary": None,
            "sku": product_id,
            "upc": upc,
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
            "reviews": reviews,
            "rating": rating,
            "sold_count": None,
            "shipping_fee": shipping_fee,
            "shipping_days_min": shipping_days_min,
            "shipping_days_max": shipping_days_max,
            "weight": weight,
            "width": None,
            "height": None,
            "length": None
        }
