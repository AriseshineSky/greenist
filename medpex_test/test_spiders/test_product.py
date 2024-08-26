import unittest
from scrapy.utils.test import get_crawler
from scrapy.http import Request, Response, HtmlResponse
from greenist.spiders.medpex import MedpexSpider


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.crawler = get_crawler(MedpexSpider)
        self.spider = self.crawler._create_spider()

    def test_available_product_v1(self):
        url = "https://www.medpex.de/ibuhexal-akut-400mg/3161577"
        body = None
        with open(
            "medpex_test/pages/ibuhexal-akut-400mg_3161577.html",
            "rb",
        ) as file:
            body = file.read()
        response = HtmlResponse(
            url=url,
            body=body,
        )
        result = list(self.spider.parse(response))
        self.assertEqual(len(result), 1)
        product = result[0]
        target_product = {
            "url": "https://www.medpex.de/ibuhexal-akut-400mg/3161577",
            "source": "medpex",
            "product_id": "3161577", # Artikelnummer意为商品号
            "existence": True,
            "title": "IbuHEXAL akut 400mg",
            # "description": None,
            "sku": "3161577",
            "upc": None,
            "brand": "Hexal AG",
            "categories": 'kopfschmerzen-migraene',
            "images": "https://images.medpex.de/medias/72727/It5BStqURhV27DeVnFIVka-30.jpg;https://images.medpex.de/medias/72814/FJvXu8T73TQH2cDxEFIVka-30.jpg;https://images.medpex.de/medias/72876/xAlf73Uk4TQH2cDxEFIVka-30.jpg;https://images.medpex.de/medias/73056/c0ZRzoWS7TQH2cDxEFIVka-30.jpg;https://images.medpex.de/medias/31287/mE4AiNFVjEcfXLf7q5eN1d-30.jpg;https://images.medpex.de/medias/31347/WCLME2B6lEcfXLf7q5eN1d-30.jpg;https://images.medpex.de/medias/31397/MRtIlws6mEcfXLf7q5eN1d-30.jpg;https://images.medpex.de/medias/31441/7Siz0AmXmEcfXLf7q5eN1d-30.jpg;https://images.medpex.de/medias/31482/lJCl66xLnEcfXLf7q5eN1d-30.jpg;https://images.medpex.de/medias/31516/Yu4J7xQqoEcfXLf7q5eN1d-30.jpg;https://images.medpex.de/medias/31539/ZefUpTxToEcfXLf7q5eN1d-30.jpg",
            "videos": None,
            "price": 7.85, # currency 1.11
            "available_qty": None,
            "reviews": 67,
            "rating": 5,
            "shipping_fee": 3.32,
            "shipping_days_min": 1,
            "shipping_days_max": 2,
            "weight": None,
        }

        keys = [
            "url",
            "source",
            "product_id",
            "existence",
            "title",
            # "description",
            "sku",
            "upc",
            "brand",
            "categories",
            "images",
            "videos",
            "price",
            "available_qty",
            "reviews",
            "rating",
            "shipping_fee",
            "shipping_days_min",
            "shipping_days_max",
            "weight",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])

    def test_available_product_v2(self):
        url = "https://www.medpex.de/wick-medinait-erkaeltungssirup-fuer-die-nacht/1689009"
        body = None
        with open(
            "medpex_test/pages/wick-medinait-erkaeltungssirup-fuer-die-nacht_1689009.html",
            "rb",
        ) as file:
            body = file.read()
        response = HtmlResponse(
            url=url,
            body=body,
        )
        result = list(self.spider.parse(response))
        self.assertEqual(len(result), 1)
        product = result[0]
        target_product = {
            "url": "https://www.medpex.de/wick-medinait-erkaeltungssirup-fuer-die-nacht/1689009",
            "source": "medpex",
            "product_id": "1689009", # Artikelnummer意为商品号
            "existence": True,
            "title": "WICK MediNait Erkältungssirup für die Nacht",
            # "description": None,
            "sku": "1689009",
            "upc": "4066447774344",
            "brand": "WICK Pharma - Zweigniederlassung der Procter & Gamble GmbH",
            "categories": 'erkaeltungspraeparate',
            "images": "https://images.medpex.de/medias/18721/FVZzEiZCDVm57DeVnFIVka-30.jpg;https://images.medpex.de/medias/48038/gacvXlUfTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/48135/g6DqtGihTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/48231/18u4Us7jTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/48322/qjOCOVykTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/48403/6Ahkou5mTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/48470/5fp3NjkoTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/77683/tdLjxywpTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/48500/UHOACu9WnhgdA3wTabMt68-30.jpg",
            "videos": "https://www.youtube-nocookie.com/embed/xro6sMuk0pI?controls=0",
            "price": 18.08, # currency 1.11
            "available_qty": None,
            "reviews": 329,
            "rating": 5,
            "shipping_fee": 3.32,
            "shipping_days_min": 1,
            "shipping_days_max": 2,
            "weight": None,
        }

        keys = [
            "url",
            "source",
            "product_id",
            "existence",
            "title",
            # "description",
            "sku",
            "upc",
            "brand",
            "categories",
            "images",
            "videos",
            "price",
            "available_qty",
            "reviews",
            "rating",
            "shipping_fee",
            "shipping_days_min",
            "shipping_days_max",
            "weight",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])

    def test_available_product_v3(self):
        url = "https://www.medpex.de/gingonin-120mg/12724861"
        body = None
        with open(
            "medpex_test/pages/gingonin-120mg_12724861.html",
            "rb",
        ) as file:
            body = file.read()
        response = HtmlResponse(
            url=url,
            body=body,
        )
        result = list(self.spider.parse(response))
        self.assertEqual(len(result), 1)
        product = result[0]
        target_product = {
            "url": "https://www.medpex.de/gingonin-120mg/12724861",
            "source": "medpex",
            "product_id": "12724861", # Artikelnummer意为商品号
            "existence": True,
            "title": "Gingonin 120mg",
            # "description": None,
            "sku": "12724861",
            "upc": None,
            "brand": "TAD Pharma GmbH",
            "categories": 'gedaechtnis-konzentration',
            "images": "https://images.medpex.de/medias/18721/FVZzEiZCDVm57DeVnFIVka-30.jpg;https://images.medpex.de/medias/48038/gacvXlUfTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/48135/g6DqtGihTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/48231/18u4Us7jTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/48322/qjOCOVykTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/48403/6Ahkou5mTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/48470/5fp3NjkoTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/77683/tdLjxywpTN0dA3wTabMt68-30.jpg;https://images.medpex.de/medias/48500/UHOACu9WnhgdA3wTabMt68-30.jpg",
            "videos": "https://www.youtube-nocookie.com/embed/n2jeAkHuVVo?controls=0",
            "price": 23.60, # currency 1.11
            "available_qty": 3,
            "reviews": 6,
            "rating": 5,
            "shipping_fee": 0.00,
            "shipping_days_min": 1,
            "shipping_days_max": 2,
            "weight": 0.40,
        }

        keys = [
            "url",
            "source",
            "product_id",
            "existence",
            "title",
            # "description",
            "sku",
            "upc",
            "brand",
            "categories",
            "images",
            "videos",
            "price",
            "available_qty",
            "reviews",
            "rating",
            "shipping_fee",
            "shipping_days_min",
            "shipping_days_max",
            "weight",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])

    def test_available_product_v4(self):
        url = "https://www.medpex.de/voltaren-schmerzgel/5388090"
        body = None
        with open(
            "medpex_test/pages/voltaren-schmerzgel_5388090.html",
            "rb",
        ) as file:
            body = file.read()
        response = HtmlResponse(
            url=url,
            body=body,
        )
        result = list(self.spider.parse(response))
        self.assertEqual(len(result), 1)
        product = result[0]
        target_product = {
            "url": "https://www.medpex.de/voltaren-schmerzgel/5388090",
            "source": "medpex",
            "product_id": "5388090", # Artikelnummer意为商品号
            "existence": True,
            "title": "VOLTAREN Schmerzgel",
            # "description": None,
            "sku": "5388090",
            "upc": None,
            "brand": "GlaxoSmithKline Consumer Healthcare GmbH & Co. KG - OTC Medicines",
            "categories": 'gelenke-muskeln-gelenke',
            "images": "https://images.medpex.de/medias/85477/qTnIGjuPJIz57DeVnFIVka-30.jpg;https://images.medpex.de/medias/85477/sVk78A8NLIz57DeVnFIVka-30.jpg;https://images.medpex.de/medias/85477/ngO00VXKSj2N2cDxEFIVka-30.jpg",
            "videos": None,
            "price": 29.96, # currency 1.11
            "available_qty": None,
            "reviews": 800,
            "rating": 5,
            "shipping_fee": 0.00,
            "shipping_days_min": 1,
            "shipping_days_max": 2,
            "weight": 0.66,
        }

        keys = [
            "url",
            "source",
            "product_id",
            "existence",
            "title",
            # "description",
            "sku",
            "upc",
            "brand",
            "categories",
            "images",
            "videos",
            "price",
            "available_qty",
            "reviews",
            "rating",
            "shipping_fee",
            "shipping_days_min",
            "shipping_days_max",
            "weight",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])

    def test_available_product_v5(self):
        url = "https://www.medpex.de/ohrenreiniger-m-holzgriff-schlaufe-aus-inox/18049538"
        body = None
        with open(
            "medpex_test/pages/ohrenreiniger-m-holzgriff-schlaufe-aus-inox_18049538.html",
            "rb",
        ) as file:
            body = file.read()
        response = HtmlResponse(
            url=url,
            body=body,
        )
        result = list(self.spider.parse(response))
        self.assertEqual(len(result), 1)
        product = result[0]
        target_product = {
            "url": "https://www.medpex.de/ohrenreiniger-m-holzgriff-schlaufe-aus-inox/18049538",
            "source": "medpex",
            "product_id": "18049538", # Artikelnummer意为商品号
            "existence": True,
            "title": "OHRENREINIGER m.Holzgriff Schlaufe aus Inox",
            # "description": None,
            "sku": "18049538",
            "upc": None,
            "brand": "Param GmbH",
            "categories": None,
            "images": None,
            "videos": None,
            "price": 3.21, # currency 1.11
            "available_qty": None,
            "reviews": 0,
            "rating": None,
            "shipping_fee": 3.32,
            "shipping_days_min": 1,
            "shipping_days_max": 2,
            "weight": None,
        }

        keys = [
            "url",
            "source",
            "product_id",
            "existence",
            "title",
            # "description",
            "sku",
            "upc",
            "brand",
            "categories",
            "images",
            "videos",
            "price",
            "available_qty",
            "reviews",
            "rating",
            "shipping_fee",
            "shipping_days_min",
            "shipping_days_max",
            "weight",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])


if __name__ == "__main__":
    unittest.main()
