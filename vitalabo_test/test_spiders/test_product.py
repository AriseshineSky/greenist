import json
import unittest
from scrapy.utils.test import get_crawler
from scrapy.http import Request, Response, HtmlResponse
from greenist.spiders.vitalabo import VitalaboSpider


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.crawler = get_crawler(VitalaboSpider)
        self.spider = self.crawler._create_spider()

    def test_variable_produkt(self):
        url = "https://www.vitalabo.com/natures-plus/source-of-life-animal-parade"
        body = None
        with open(
            "vitalabo_test/pages/source-of-life-animal-parade.htm",
            "rb"
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
            "product_id": "DS-29972",
            "url": "https://www.vitalabo.com/natures-plus/source-of-life-animal-parade",
            "source": "Vitalabo",
            "existence": True,
            "title": "Animal Parade 180 Chewable Multivitamins, Cherry (180 chewable tablets)",
            "images": "https://va.nice-cdn.com/upload/image/product/large/default/75722_63cdfc9e.768x768.jpg;https://va.nice-cdn.com/upload/image/product/large/default/75723_0d774822.768x768.jpg",
            "description_en": None,
            "summary": None,
            "upc": "097467299726",
            "sku": "DS-29972",
            "brand": "NaturesPlus",
            "specifications": None,
            "categories": 'Brands > NaturesPlus®',
            "price": 47.16, # currency 1.11
            "videos": None,
            "shipping_fee": 0.00,
            "available_qty": 2,
            "reviews": 31,
            "rating": 4.7,
            "weight": 0.77, # kg -> lb 2.20462
            "options": None,
            "variants": None,
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
            # "description_en",
            # "specifications",
            "images",
            "price",
            "categories",
            "available_qty",
            "reviews",
            "rating",
            "weight",
            # "options",
            # "variants",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])


    def test_unavailable_product(self):
        url = "https://www.vitalabo.com/natures-plus/animal-parade-inner-ear-support"
        body = None
        with open(
            "vitalabo_test/pages/animal-parade-inner-ear-support.htm",
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
            "product_id": "DS-29949",
            "url": "https://www.vitalabo.com/natures-plus/animal-parade-inner-ear-support",
            "source": "Vitalabo",
            "existence": False,
            "title": "Animal Parade Inner Ear Support - Sugar-Free, 90 chewable tablets",
            "images": "https://va.nice-cdn.com/upload/image/product/large/default/75587_57609dee.768x768.jpg;https://va.nice-cdn.com/upload/image/product/large/default/75588_26d494a9.768x768.jpg;https://va.nice-cdn.com/upload/image/product/large/default/75589_c81cbe37.768x768.jpg",
            "description_en": None,
            "summary": None,
            "upc": "097467299498",
            "sku": "DS-29949",
            "brand": "NaturesPlus",
            "specifications": None,
            "categories": 'Brands > NaturesPlus®',
            "price": 36.06, # currency 1.11
            "videos": None,
            "shipping_fee": 5.44,
            "available_qty": 0,
            "reviews": 3,
            "rating": 5.0,
            "weight": 0.42, # kg -> lb 2.20462 
            "options": None,
            "variants": None,
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
            # "description_en",
            # "specifications",
            "images",
            "price",
            "categories",
            "available_qty",
            "reviews",
            "rating",
            "weight",
            "options",
            "variants",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])


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
            "product_id": "DS-3085",
            "url": "https://www.vitalabo.com/natures-plus/ultra-prenatal",
            "source": "Vitalabo",
            "existence": True,
            "title": "Ultra Prenatal®, 180 tablets",
            "images": "https://va.nice-cdn.com/upload/image/product/large/default/15257_33ceb058.768x768.jpg;https://va.nice-cdn.com/upload/image/product/large/default/76617_dbd755ec.768x768.jpg;https://va.nice-cdn.com/upload/image/product/large/default/76618_eaa8a183.768x768.jpg",
            "description_en": None,
            "summary": None,
            "upc": "097467030855",
            "sku": "DS-3085",
            "brand": "NaturesPlus",
            "specifications": None,
            "categories": 'Brands > NaturesPlus®',
            "price": 72.14, # currency 1.11
            "videos": None,
            "shipping_fee": 0.00,
            "available_qty": 3,
            "reviews": 12,
            "rating": 5.0,
            "weight": 1.03, # kg -> lb 2.20462
            "options": None,
            "variants": None,
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
            # "description_en",
            # "specifications",
            "images",
            "price",
            "categories",
            "available_qty",
            "reviews",
            "rating",
            "weight",
            "options",
            "variants",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])


    def test_available_product_v2(self):
        url = "https://www.vitalabo.com/natures-plus/ultra-bromelain"
        body = None
        with open(
            "vitalabo_test/pages/ultra-bromelain.html",
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
            "product_id": "DS-4406",
            "url": "https://www.vitalabo.com/natures-plus/ultra-bromelain",
            "source": "Vitalabo",
            "existence": True,
            "title": "Ultra Bromelain, 60 tablets",
            "images": "https://va.nice-cdn.com/upload/image/product/large/default/70020_6ddfe281.768x768.jpg;https://va.nice-cdn.com/upload/image/product/large/default/70021_1ca5f342.768x768.jpg",
            "description_en": None,
            "summary": None,
            "upc": "097467044067",
            "sku": "DS-4406",
            "brand": "NaturesPlus",
            "specifications": None,
            "categories": 'Brands > NaturesPlus®',
            "price": 61.04, # currency 1.11
            "videos": None,
            "shipping_fee": 0.00,
            "available_qty": 4,
            "reviews": 11,
            "rating": 4.0,
            "weight": 0.26, # kg -> lb 2.20462
            "options": None,
            "variants": None,
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
            # "description_en",
            # "specifications",
            "images",
            "price",
            "categories",
            "available_qty",
            "reviews",
            "rating",
            "weight",
            "options",
            "variants",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])


if __name__ == "__main__":
    unittest.main()
