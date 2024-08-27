from datetime import datetime

import scrapy
from scrapy.http import Request, Response, HtmlResponse


# python3 -m dm_test.test_spiders.test_product
class DmSpider(scrapy.Spider):
    name = "dm_spider"
    allowed_domains = ["dm.de"]
    start_urls = ["https://products.dm.de/"]

    def parse(self, response: HtmlResponse):
        prod_info = response.json()
        print(prod_info)

        url = 'https://www.dm.de'+prod_info['self']
        product_id = prod_info['dan']
        
        existence = False
        if prod_info['availability']['purchasable']:
            existence = True

        title = prod_info['title']['headline']

        # TODO
        description = None

        upc = prod_info['gtin']
        brand = prod_info['title']['brand']
        categories = " > ".join(prod_info['breadcrumbs'])
        
        images = None
        if 'images' in prod_info:
            images = ';'.join([img['zoomSrc'] for img in prod_info['images']])
        
        videos = None
        if 'videos' in prod_info:
            videos = ';'.join([v['iframeSrc'] for v in prod_info['videos']])

        yield {
            "date": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            "url": url,
            "source": "dm",
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
            "images": images,
            "videos": videos,
        }
