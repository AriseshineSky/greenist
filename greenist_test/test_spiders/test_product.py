import json
import unittest
from scrapy.utils.test import get_crawler
from scrapy.http import Request, Response, HtmlResponse
from greenist.spiders.product import ProductSpider


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.crawler = get_crawler(ProductSpider)
        self.spider = self.crawler._create_spider()

    def test_unavailable_product(self):
        url = "https://www.greenist.de/janur-kokosbluetenzucker-im-nimmersattsack-1kg.html"
        body = None
        with open(
            "greenist_test/pages/janur-kokosbluetenzucker-im-nimmersattsack-1kg.html",
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
            "url": "https://www.greenist.de/janur-kokosbluetenzucker-im-nimmersattsack-1kg.html",
            "source": "Greenist",
            "existence": False,
            "title": "Kokosblütenzucker im Nimmersattsack, 1kg",
            "images": "https://www.greenist.de/media/image/7a/5d/50/janur-kokosbluetenzucker-1kg-front_600x600.webp",
            "description_en": None,
            "summary": None,
            "upc": '4260437940409',
            "sku": None,
            "brand": "Janur",
            "specifications": None,
            "categories": "Vitalfood > Natürlich Süßen > Zuckeralternativen",
            "reviews": 0,
            "rating": None,
            "price": None,
            "videos": None,
            "shipping_fee": 0.00,
            "shipping_days_min": None,
            "shipping_days_max": None,
            "product_id": "JAN-KBZU1",
            "weight": 2.65,
            "width": None,
            "height": None,
            "length": None
        }

        keys = [
            "existence",
            "product_id",
            "sku",
            "url",
            "source",
            "brand",
            "title",
            "shipping_fee",
            "shipping_days_min",
            "shipping_days_max",
            # "specifications",
            "images",
            "price",
            "categories",
            "reviews",
            "rating",
            "weight",
            "width",
            "height",
            "length"
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])

    def test_available_product_v1(self):
        url = "https://www.greenist.de/bio-planete-bio-arganoel-nativ-100ml.html"
        body = None
        with open(
            "greenist_test/pages/bio-planete-bio-arganoel-nativ-100ml.html",
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
            "url": "https://www.greenist.de/bio-planete-bio-arganoel-nativ-100ml.html",
            "source": "Greenist",
            "existence": True,
            "title": "Bio Arganöl, nativ, 100ml",
            "images": "https://www.greenist.de/media/image/4b/ed/df/bio-planete-bio-arganoel-nativ-100ml-front-neu_600x600.webp",
            "description_en": None,
            "summary": None,
            "upc": '3445020003278',
            "sku": None,
            "brand": "Bio Planète",
            "specifications": None,
            "categories": "Vitalfood > Öle & Essig > Öle",
            "reviews": 3,
            "rating": 5.00,
            "price": 15.53, # currency 1.11
            "videos": None,
            "shipping_fee": 0.00,
            "shipping_days_min": 1,
            "shipping_days_max": 3,
            "product_id": "BPL-ARGA",
            "weight": 0.59,
            "width": 1.65,
            "height": 6.22,
            "length": 1.65
        }

        keys = [
            "existence",
            "product_id",
            "sku",
            "url",
            "source",
            "brand",
            "title",
            "shipping_fee",
            "shipping_days_min",
            "shipping_days_max",
            # "specifications",
            "images",
            "price",
            "categories",
            "reviews",
            "rating",
            "weight",
            "width",
            "height",
            "length"
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])


if __name__ == "__main__":
    unittest.main()
