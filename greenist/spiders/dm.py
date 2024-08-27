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

        url = 'https://www.dm.de'+prod_info['self']
        product_id = str(prod_info['dan'])
        
        existence = False
        if prod_info['availability']['purchasable']:
            existence = True

        title = prod_info['title']['headline']

        # TODO
        description = None

        if 'descriptionGroups' in prod_info:
            description = '<div class="dm-descr">\n'

            for descr in prod_info['descriptionGroups']:
                if descr['header'] == 'Anschrift des Unternehmens': # 过滤制造元资料
                    continue

                description += '  <div>\n'
                description += f'    <h2>{descr["header"]}</h2>\n'
                
                for dcb in descr['contentBlock']:
                    description += '      <div>\n'

                    if 'texts' in dcb:
                        for dt in dcb['texts']:
                            description += f'        <div>{dt}</div>\n'
                    if 'images' in dcb:
                        for img in dcb['images']:
                            description += f'        <img src="{img["src"]}">\n'
                    if 'table' in dcb:
                        description += f'        <table>\n'
                        description += f'          <tr><th>{dcb["table"][0][0]}</th><th>{dcb["table"][0][1]}</th></tr>\n'
                        for zeile in dcb['table'][1:]:
                            description += f'          <tr><td>{zeile[0]}</td><td>{zeile[1]}</td></tr>\n'
                        description += f'        </table>\n'
                    if 'bulletpoints' in dcb:
                        description += f'        <ul>\n'
                        for li in dcb['bulletpoints']:
                            description += f'          <li>{li}</li>\n'
                        description += f'        </ul>\n'
                    
                    description += '      </div>\n'
                
                description += '  </div>\n'

            description += '</div>\n' 
        # print(description)

        upc = str(prod_info['gtin'])
        brand = prod_info['title']['brand']
        categories = " > ".join(prod_info['breadcrumbs'])
        
        images = None
        if 'images' in prod_info:
            images = ';'.join([img['zoomSrc'] for img in prod_info['images']])
        
        videos = None
        if 'videos' in prod_info:
            videos = ';'.join([v['iframeSrc'] for v in prod_info['videos']])

        price = round(float(prod_info['price']['price'])*1.11, 2)

        available_qty = None
        if not existence:
            available_qty = 0
        
        reviews = prod_info['rating']['ratingCount']
        rating = round(prod_info['rating']['ratingValue'], 1)

        weight = None
        length = None
        einheit = None
        menge = None

        if 'basePriceUnit' in prod_info['price']:
            einheit = prod_info['price']['basePriceUnit'].lower()
        else:
            einheit = title.split()[-1].strip().lower() # 标题通常以量与单位结束
        menge = float(prod_info['price']['basePriceRelNetQuantity'])
        
        if (einheit == 'kg') or (einheit == 'l'):
            weight = round(menge*2.204623, 2)
        elif (einheit == 'g') or (einheit == 'ml'):
            weight = round(menge*0.002205, 2)
        elif (einheit == 'm'):
            length = round(menge*39.37008, 2)
        elif (einheit == 'cm'):
            length = round(menge*0.393701, 2)

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
            "price": price,
            "available_qty": available_qty,
            "options": None,
            "variants": None,
            "returnable": False,
            "reviews": reviews,
            "rating": rating,
            "sold_count": None,
            "shipping_fee": 5.49,
            "shipping_days_min": 2,
            "shipping_days_max": 3,
            "weight": weight,
            "width": None,
            "height": None,
            "length": length
        }
