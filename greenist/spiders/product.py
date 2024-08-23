from datetime import datetime
from re import findall

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
        product_id = response.css('input[name="ordernumber"]::attr(value)').get().strip()

        existence = False
        exist_sel = response.css('meta[itemprop="og:availability"]::attr(href)')
        if exist_sel and (exist_sel.get().strip() == 'instock'):
            existence = True

        title = response.css('div.h1::text').get().strip()
        images = response.css('div.product--image-container source[type="image/webp"]::attr(srcset)').get().strip()

        upc = None
        nt_sels = response.css('div.nutrition--title')
        ean_i = -1
        for s in range(len(nt_sels)):
            if nt_sels[s].css('::text').get().strip() == 'EAN':
                ean_i = s
                break
        if ean_i >= 0:
            upc = response.css('div.nutrition--value')[ean_i].css('p::text').get().strip()

        brand = response.css('meta[property="product:brand"]::attr(content)').get().strip()

        cat_list = [cat.get().strip() for cat in response.css('span.breadcrumb--title::text')[1:]]
        categories = " > ".join(cat_list)

        price = None
        price_sel = response.css('meta[itemprop="price"]::attr(content)')
        if price_sel:
            price = round(float(price_sel.get().strip())*1.11, 2)

        reviews = 0
        rev_sel = response.css('meta[itemprop="ratingCount"]::attr(content)')
        if rev_sel:
            reviews = int(rev_sel.get().strip())

        rating = None
        rat_sel = response.css('meta[itemprop="ratingValue"]::attr(content)')
        if rat_sel:
            rating = round(float(rat_sel.get().strip())/2.0, 2) # 10分制 -> 5分制
        
        def extract_shipping_days(txt: str):
            match1 = findall(r'(\d+)-(\d+) Werktag', txt)
            if match1:
                return (int(match1[0][0]), int(match1[0][1]))
            match2 = findall(r'(\d+) Werktag', txt)
            if match2:
                return (int(match1[0]), int(match1[0]))
            return (None, None)

        shipping_days_min = None
        shipping_days_max = None
        ship_sel = response.css('span.delivery--text span')
        if ship_sel:
            ship_txt = ship_sel[1].css('::text').get().strip()
            ship_match = extract_shipping_days(ship_txt)
            shipping_days_min, shipping_days_max = ship_match

        weight = None
        weight_sel = response.css('meta[itemprop="weight"]::attr(content)')
        if weight_sel:
            weight = round(float(weight_sel.get().strip()[:-3])*2.20462, 2)

        width = None
        width_sel = response.css('meta[itemprop="width"]::attr(content)')
        if width_sel:
            width = round(float(width_sel.get().strip()[:-3])*0.393701, 2)
        
        height = None
        height_sel = response.css('meta[itemprop="height"]::attr(content)')
        if height_sel:
            height = round(float(height_sel.get().strip()[:-3])*0.393701, 2)

        length = None
        length = None
        length_sel = response.css('meta[itemprop="depth"]::attr(content)')
        if length_sel:
            length = round(float(length_sel.get().strip()[:-3])*0.393701, 2)

        yield {
            "date": date,
            "url": url,
            "source": "Greenist",
            "product_id": product_id,
            "existence": existence,
            "title": title,
            "title_en": None,
            "description_en": None,
            "summary": None,
            "sku": None,
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
            "shipping_fee": 0.00,
            "shipping_days_min": shipping_days_min,
            "shipping_days_max": shipping_days_max,
            "weight": weight,
            "width": width,
            "height": height,
            "length": length
        }
