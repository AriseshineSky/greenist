from datetime import datetime
from json import loads
from re import findall

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
        except:
            return

        url = 'https://www.docmorris.de'+prod_info['url']
        product_id = prod_info['productId']
        existence = prod_info['available']
        title = prod_info['name']

        description = '<div class="docmorris-descr">\n'

        if prod_info['marketingText']:
            description += '  <div>\n'
            description += '    <h2>Produktinformationen</h2>\n'
            description += f'    {prod_info["marketingText"]}'
            description += '  </div>\n'

        if prod_info['pharmaceuticalInformation']:
            description += '  <div>\n'
            description += '    <h2>Gebrauchsinformationen & Pflichtangaben</h2>\n'
            
            for i, pi in enumerate(prod_info['pharmaceuticalInformation']):
                ut = pi['type']
                inh = pi['content']

                h3 = f'Info{i}'
                if ut == 'DOSAGE':
                    h3 = 'Dosierung'
                elif ut == 'WARNINGS':
                    h3 = 'Warnhinweise & Hilfsstoffe'
                elif ut == 'INTERACTIONS':
                    h3 = 'Wechselwirkungen'
                elif ut == 'PATIENT_INFORMATION':
                    h3 = 'Patientenhinweise'
                elif ut == 'SIDE_EFFECTS':
                    h3 = 'Nebenwirkungen'
                elif ut == 'APPLICATION_AREAS':
                    h3 = 'Anwendungsgebiete'
                elif ut == 'LACTATION':
                    h3 = 'Stillzeit'
                elif ut == 'MODE_OF_USE':
                    h3 = 'Anwendungshinweise'
                elif ut == 'CONTRAINDICATIONS':
                    h3 = 'Gegenanzeigen'
            
                description += f'    <h3>{h3}</h3>\n'
                description += f'    <div>{inh}</div>\n'
            
            description += '  </div>\n'

        if (prod_info['composition']) and ((prod_info['composition'].get('activeIngredients')) or (prod_info['composition'].get('additives'))):
            description += '  <div>\n'
            description += '    <h2>Produktzusammensetzung</h2>\n'

            if prod_info['composition'].get('activeIngredients'):
                description += '    <h3>Wirkstoffe</h3>\n'
                description += '    <table>\n'

                for ai in prod_info['composition']['activeIngredients']:
                    description += f'      <tr><th scope=\"row\">{ai["name"]}</th><td>{ai["quantity"]}</td></tr>\n'

                description += '    </table>\n'

            if prod_info['composition'].get('additives'):
                description += '    <h3>Hilfsstoffe</h3>\n'
                description += '    <table>\n'

                for ad in prod_info['composition']['additives']:
                    description += f'      <tr><th scope=\"row\">{ad["name"]}</th><td>{ad["quantity"]}</td></tr>\n'

                description += '    </table>\n'

            description += '  </div>\n'

        description += '</div>\n'
        print(description)

        # https://squareup.com/us/en/the-bottom-line/operating-your-business/stock-keeping-unit#:~:text=SKU%20stands%20for%20%E2%80%9Cstock%20keeping,has%20a%20unique%20SKU%20number.
        sku = prod_info['readableId'] # SKU通常为8位

        upc = prod_info['code']
        brand = prod_info['brand']

        categories = None
        if prod_info['breadcrumbs']:
            categories = " > ".join([bc['name'] for bc in prod_info['breadcrumbs']])

        images = None
        if prod_info['images']:
            images = ";".join([img['variants']['420']['formats']['webp']['resolutions']['2x']['url'] for img in prod_info['images']])

        price_eu = prod_info['prices']['salesPrice']['value']
        price = round(price_eu*1.11, 2)

        available_qty = None
        if not existence:
            available_qty = 0
        
        reviews = prod_info['reviewCount'] if prod_info['reviewCount'] else 0
        rating = round(prod_info['rating'], 1) if (prod_info['rating'] is not None) else None
        shipping_fee = 0.00 if price_eu >= 19.00 else 3.89 # 19欧元及以上免运费

        # 解析重量
        weight = None
        menge, einheit = prod_info['packagingSize'].strip().lower().split()
        if (einheit == 'ml') or (einheit == 'g'):
            weight = round(float(menge)*0.002205, 2)
        elif (einheit == 'l') or (menge == 'kg'):
            weight = round(float(menge)*2.204623, 2)
        else:
            ep, _ = prod_info['baseprice'].strip().lower().split()
            m = price_eu / float(ep.replace('.', '').replace(',', '.'))
            if (prod_info['baseprice'].endswith('/g')) or (prod_info['baseprice'].endswith('/ml')):
                weight = round(m*0.002205, 2)
            elif (prod_info['baseprice'].endswith('/kg')) or (prod_info['baseprice'].endswith('/l')):
                weight = round(m*2.204623, 2)

        width, length = self.parse_dimensions(title.lower())

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
            "height": None,
            "length": length
        }

    def parse_dimensions(self, titel: str) -> tuple:
        """
        由标题解析长宽
        """

        dimensions = [None, None]
        width = None
        length = None

        match1 = findall(r'(\d+)\s*([a-zA-Z]*)\s*[Xx]\s*(\d+)\s*([a-zA-Z]+)', titel)
        match2 = findall(r'(\d+)\s*([a-zA-Z]+)', titel)

        if match1:
            amounts = [match1[0][0], match1[0][2]]

            unit2 = match1[0][3]
            unit1 = match1[0][1] if match1[0][1] else unit2
            units = [unit1, unit2]

            for i, (am, un) in enumerate(zip(amounts, units)):
                if un == 'cm':
                    dimensions[i] = round(float(am)*0.393701, 2)
                elif un == 'm':
                    dimensions[i] = round(float(am)*39.37008, 2)
        elif match2:
            am, un = match2[0]
            if un == 'cm':
                length = round(float(am)*0.393701, 2)
            elif un == 'm':
                length = round(float(am)*39.37008, 2)

        if (dimensions[0] is not None) and (dimensions[1] is not None):
            if dimensions[0] > dimensions[1]:
                width = dimensions[1]
                length = dimensions[0]
            else:
                width = dimensions[0]
                length = dimensions[1]

        return (width, length)
