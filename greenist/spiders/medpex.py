from datetime import datetime
from json import loads

import scrapy
from scrapy.http import Request, Response, HtmlResponse


# python3 -m medpex_test.test_spiders.test_product
class MedpexSpider(scrapy.Spider):
    name = "medpex_spider"
    allowed_domains = ["medpex.de"]
    start_urls = ["https://www.medpex.de"]

    def parse(self, response: HtmlResponse):
        # breakpoint()

        url = response.css('meta[property="og:url"]::attr(content)').get().strip()
        product_id = url.split('/')[-1]

        existence = False
        if 'instock' in response.css('link[itemprop="availability"]::attr(href)').get().lower():
            existence = True

        name, inhalt = response.css('h1[itemprop="name"]::text').get().strip().rsplit(', ', 1)
        title = name.strip()

        infos = response.css('div.clearfix > div.information > *')
        
        video_i = -1
        beschr_i = -1
        hinw_i = -1

        for i, info in enumerate(infos):
            tag = info.root.tag

            if (tag == 'h2'):
                h2 = info.css('::text').get().strip()
                if (h2 == 'Video'):
                    video_i = i+1
                elif (h2 == 'Beschreibung'):
                    beschr_i = i+1
                elif (h2 == 'Hinweis'):
                    hinw_i = i+1
            if (video_i >= 0) and (beschr_i >= 0) and (hinw_i >= 0):
                break

        pz_titel = response.css('div#drugInformationContainer div.box-title > h2')
        pz_inhalte = response.css('div#drugInformationContainer div.box-content')

        description = '<div class="medpex-descr">\n'

        if beschr_i >= 0:
            description += '<h2>Beschreibung</h2>\n'
            description += infos[beschr_i].get().replace('\r', '').replace('\n', '')
            description += '\n\n'
        if hinw_i >= 0:
            description += '<h2>Hinweis</h2>'
            description += infos[hinw_i].get().replace('\r', '').replace('\n', '')
            description += '\n\n'

        if pz_titel:
            description += "<h2>Pflichtangaben & Zusatzinformationen</h2>\n<div>\n"

            for j, (tit, inh) in enumerate(zip(pz_titel, pz_inhalte)):
                description += f"<h2>{tit.css('::text').get().strip()}</h2>\n"
                description += inh.get().strip()
                description += '\n'
            
            description += "</div>"

        description += '</div>'

        sku = product_id
        
        upc = None
        upc_sel = response.css('span[itemprop="gtin14"]')
        if upc_sel:
            upc = upc_sel.css("::text").get().strip()

        brand = response.css('span[itemprop="brand"]::text').get().strip()

        categories = None
        prod_det = response.css('div#productDetails::attr(data-tracking-product-main-category-code)')
        if prod_det:
            categories = prod_det.get().strip()

        images = None
        img_sel = response.css('div#more-images > a')
        if img_sel:
            images = ";".join([img.css('::attr(href)').get().strip() for img in img_sel])
        
        videos = None
        if video_i >= 0:
            videos = infos[video_i].css('iframe::attr(src)').get().strip()
        
        price = round(float(response.css('meta[itemprop="price"]::attr(content)').get().strip())*1.11, 2)

        available_qty = None
        if not existence:
            available_qty = 0
        else:
            verf = response.css('div.stock--available::text').get().strip().lower().rsplit(maxsplit=2)
            if (verf[0] == 'nur noch'):
                available_qty = int(verf[1].strip())

        reviews = 0
        rev_sel = response.css('div.review span[itemprop="reviewCount"]')
        if rev_sel:
            reviews = int(rev_sel.css('::text').get().strip())
        
        rating = None
        rat_sel = response.css('meta[itemprop="ratingValue"]')
        if rat_sel:
            rating = int(rat_sel.css('::attr(content)').get().strip())
        
        # https://support.medpex.de/hc/de/articles/4405361639186-Versandkosten-Versandinformationen
        shipping_fee = 3.32 # 统一运费
        if 'frei' in response.css(f'a#shipping-{product_id}::text').get().strip():
            shipping_fee = 0.00

        weight = None
        inhalt = inhalt.strip().lower().split(' ')
        if ('milliliter' in inhalt) or ('gramm' in inhalt):
            weight = round(float(inhalt[0].strip())/453.592, 2)

        yield {
            "date": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            "url": url,
            "source": "medpex",
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
            "videos": videos,
            "price": price,
            "available_qty": available_qty,
            "options": None,
            "variants": None,
            "returnable": False,
            "reviews": reviews,
            "rating": rating,
            "sold_count": None,
            "shipping_fee": shipping_fee,
            "shipping_days_min": 1,
            "shipping_days_max": 2,
            "weight": weight,
            "width": None,
            "height": None,
            "length": None,
        }
