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
            "upc": None,
            "sku": None,
            "brand": "Janur",
            "specifications": None,
            "categories": "Vitalfood>Natürlich Süßen>Zuckeralternativen",
            "price": None,
            "videos": None,
            "shipping_fee": 0,
            "product_id": "bepanthen-augen-und-nasensalbe-5g-augen-u-nasensalbe-01578681",
        }

        keys = [
            "existence",
            "product_id",
            "sku",
            "url",
            "source",
            "existence",
            "brand",
            "product_id",
            "title",
            "shipping_fee",
            "specifications",
            "images",
            "price",
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
            "existence": False,
            "title": "Bio Arganöl, nativ, 100ml",
            "images": "https://www.greenist.de/media/image/4b/ed/df/bio-planete-bio-arganoel-nativ-100ml-front-neu_600x600.webp",
            "description_en": None,
            "summary": None,
            "upc": None,
            "sku": None,
            "brand": "Janur",
            "specifications": None,
            "categories": "Vitalfood>Natürlich Süßen>Zuckeralternativen",
            "price": 15.53,  # currency 1.11
            "videos": None,
            "shipping_fee": 0,
            "product_id": "bepanthen-augen-und-nasensalbe-5g-augen-u-nasensalbe-01578681",
        }

        keys = [
            "existence",
            "product_id",
            "sku",
            "url",
            "source",
            "existence",
            "brand",
            "product_id",
            "title",
            "shipping_fee",
            "specifications",
            "images",
            "price",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])


if __name__ == "__main__":
    unittest.main()
