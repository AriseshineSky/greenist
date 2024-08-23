import json
import unittest
from scrapy.utils.test import get_crawler
from scrapy.http import Request, Response, HtmlResponse
from greenist.spiders.vitalabo import VitalaboSpider


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.crawler = get_crawler(VitalaboSpider)
        self.spider = self.crawler._create_spider()

    def test_unavailable_product(self):
        pass
        # TODO

    def test_available_product_v1(self):
        url = "https://www.vitalabo.com/natures-plus/ultra-prenatal"
        body = None
        with open(
            "vitalabo_test/pages/ultra-prenatal.html",
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
            "url": "https://www.vitalabo.com/natures-plus/ultra-prenatal",
            "source": "Vitalabo",
            "existence": True,
            "title": "Ultra Prenatal®, 180 tablets",
            "images": "https://va.nice-cdn.com/upload/image/product/large/default/15257_33ceb058.768x768.jpg;https://va.nice-cdn.com/upload/image/product/large/default/76617_dbd755ec.768x768.jpg;https://va.nice-cdn.com/upload/image/product/large/default/76618_eaa8a183.768x768.jpg",
            "description_en": None,
            "summary": None,
            "upc": None,
            "sku": None,
            "brand": "NaturesPlus",
            "specifications": None,
            "categories": None,
            "price": 72.14, # currency 1.11
            "videos": None,
            "shipping_fee": 0.00,
        }

        keys = [
            "existence",
            "product_id",
            "sku",
            "upc",
            "url",
            "source",
            "brand",
            "title",
            "shipping_fee",
            "specifications",
            "images",
            "price",
            "categories",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])


if __name__ == "__main__":
    unittest.main()
