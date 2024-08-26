import unittest
from scrapy.utils.test import get_crawler
from scrapy.http import Request, Response, HtmlResponse
from greenist.spiders.dm import DmSpider


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.crawler = get_crawler(DmSpider)
        self.spider = self.crawler._create_spider()

    def test_variable_produkt(self):
        pass

    def test_unavailable_product(self):
        pass

    def test_available_product_v1(self):
        url = "https://www.dm.de/profissimo-hochglanz-oberflaechentuch-aus-mikrofaser-p4066447774344.html"
        body = None
        with open(
            "dm_test/pages/profissimo-hochglanz-oberflaechentuch-aus-mikrofaser-p4066447774344.html",
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
            "url": "https://www.dm.de/profissimo-hochglanz-oberflaechentuch-aus-mikrofaser-p4066447774344.html",
            "source": "dm",
            "product_id": "1713512", # Artikelnummer意为商品号
            "existence": True,
            "title": "Hochglanz-Oberflächentuch aus Mikrofaser, 1 St",
            # "description": None,
            "sku": "1713512",
            "upc": "4066447774344",
            "brand": "Profissimo",
            "categories": 'Haushalt > Putzen & Reinigen > Putztücher, Schwämme & Co.',
            "images": "https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1719794184/products/pim/4066447774344-1658996458/profissimo-hochglanz-oberflaechentuch-aus-mikrofaser;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1719794184/products/pim/4066447774344-248284225/profissimo-hochglanz-oberflaechentuch-aus-mikrofaser;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1719794184/products/pim/4066447774344-510520669/profissimo-hochglanz-oberflaechentuch-aus-mikrofaser",
            "videos": "https://www.youtube.com/watch?v=-aDVJN4etow;https://www.youtube.com/watch?v=DqMl1hoRa4A;https://www.youtube.com/watch?v=JIfS7WP734g",
            "price": 2.51, # currency 1.11
            "reviews": 1,
            "rating": 5.0,
            "shipping_fee": 5.52,
            "shipping_days_min": 2,
            "shipping_days_max": 3,
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
            "reviews",
            "rating",
            "shipping_fee",
            "shipping_days_min",
            "shipping_days_max",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])


if __name__ == "__main__":
    unittest.main()
