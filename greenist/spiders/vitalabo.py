from datetime import datetime
from json import loads

import scrapy
from scrapy.http import Request, Response, HtmlResponse


# python3 -m vitalabo_test.test_spiders.test_product
class VitalaboSpider(scrapy.Spider):
    name = "vitalabo_spider"
    allowed_domains = ["vitalabo.com"]
    start_urls = ["https://www.vitalabo.com/"]

    def parse(self, response: HtmlResponse):
        result = {
            "date": None,
            "url": None,
            "source": "Vitalabo",
            "product_id": None,
            "existence": False,
            "title": None,
            "title_en": None,
            "description_en": None,
            "summary": None,
            "sku": None,
            "upc": None,
            "brand": None,
        	"specifications": None,
            "categories": None,
            "images": None,
            "videos": None,
            "price": None,
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

        # breakpoint()

        result['date'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        result['url'] = response.css('meta[property="og:url"]::attr(content)').get().strip()

        try:
            prod_json = None
            jsons = response.css('script[type="application/ld+json"]')
            for j in jsons:
                cont = j.css('::text').get().strip()
                if ('"@type"' in cont) and ('"Product"' in cont):
                    prod_json = loads(cont)
        except:
            return

        result['product_id'] = prod_json['sku'] # 网页上“Item no.
        
        if 'instock' in prod_json['offers']['availability'].lower():
            result['existence'] = True

        result['title'] = ' '.join(response.css('h1.p-heading::text').getall()[1].strip().split())

        # TODO: description_en
        desc_sel = response.css('div.p-details > details')
        if desc_sel:
            result['description_en'] = '<div class="content--description">'
            for sel in desc_sel:
                result['description_en'] += sel.get().replace('\r', '').replace('\n', '')
            result['description_en'] += "</div>"
        print(result['description_en'])
        print()

        result['sku'] = result['product_id']
        result['upc'] = prod_json['gtin13'][1:]
        result['brand'] = prod_json['brand']['name']

        cat_sel = response.css('ul#js-breadcrumbs a')[1:-1]
        result['categories'] = " > ".join([cat.css("::text").get().strip() for cat in cat_sel])

        img_sel = response.css('div.bigslider img.product__image')
        result['images'] = ";".join([img.css("::attr(src)").get().strip().replace('256x256.jpg', '768x768.jpg') for img in img_sel])

        price_eu = float(prod_json['offers']['price'])
        result['price'] = round(price_eu*1.11, 2)

        result['available_qty'] = int(response.css('p.p-stock::attr(data-limit)').get().strip())
        result['reviews'] = int(prod_json['aggregateRating']['ratingCount'])
        result['rating'] = round(float(prod_json['aggregateRating']['ratingValue']), 1)

        ep_txt = response.css('span.p-price__perunit::text').get().strip()
        if ep_txt.endswith('kg'):
            ppk = float(ep_txt[2:-5].replace(",", "."))
            result['weight'] = round(price_eu/ppk*2.20462, 2)

        result['shipping_fee'] = round(prod_json['offers']['shippingDetails']['shippingRate']['value']*1.11, 2)
        result['shipping_days_min'] = prod_json['offers']['shippingDetails']['deliveryTime']['transitTime']['minValue']
        result['shipping_days_max'] = prod_json['offers']['shippingDetails']['deliveryTime']['transitTime']['maxValue']

        var_sel = response.css('div.p-variants')
        if var_sel:
            result['options'] = [{
                "id": None,
                "name": response.css('span.p-variants__selected__label::text').get().strip()[:-1]
            }]

        yield result
