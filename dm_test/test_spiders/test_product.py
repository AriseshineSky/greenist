import unittest
from scrapy.utils.test import get_crawler
from scrapy.http import Request, Response, HtmlResponse
from greenist.spiders.dm import DmSpider


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.crawler = get_crawler(DmSpider)
        self.spider = self.crawler._create_spider()

    def test_unavailable_produkt(self):
        url = "https://products.dm.de/product/DE/products/detail/gtin/4008137009138"
        body = None
        with open(
            "dm_test/jsons/produkt_4008137009138.json",
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
            "url": "https://www.dm.de/bad-heilbrunner-fruechtetee-heisse-zitrone-mit-limette-15-beutel-p4008137009138.html",
            "source": "dm",
            "product_id": "1425051", # Artikelnummer意为商品号
            "existence": False,
            "title": "Früchtetee Heiße Zitrone mit Limette (15 Beutel), 37,5 g",
            # "description": None,
            "sku": "1425051",
            "upc": "4008137009138",
            "brand": "Bad Heilbrunner",
            "categories": 'Gesundheit > Erkältung > Immunsystem stärken',
            "images": "https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1718668959/products/pim/4008137009138-3571267/bad-heilbrunner-fruechtetee-heisse-zitrone-mit-limette-15-beutel;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1719708700/products/pim/4008137009138-2820874/bad-heilbrunner-fruechtetee-heisse-zitrone-mit-limette-15-beutel;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1719708700/products/pim/4008137009138-2820873/bad-heilbrunner-fruechtetee-heisse-zitrone-mit-limette-15-beutel",
            "videos": None,
            "price": 3.16, # currency 1.11
            "available_qty": 0,
            "reviews": 53,
            "rating": 4.7,
            "shipping_fee": 5.49,
            "shipping_days_min": 2,
            "shipping_days_max": 3,
            "weight": 0.08, # kg -> lb 2.204623
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

    def test_available_produkt_v1(self):
        url = "https://products.dm.de/product/DE/products/detail/gtin/4066447774344"
        body = None
        with open(
            "dm_test/jsons/produkt_4066447774344.json",
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
            "videos": "https://www.youtube-nocookie.com/embed/-aDVJN4etow?rel=0&showinfo=0&modestbranding=1&playsinline=1;https://www.youtube-nocookie.com/embed/DqMl1hoRa4A?rel=0&showinfo=0&modestbranding=1&playsinline=1;https://www.youtube-nocookie.com/embed/JIfS7WP734g?rel=0&showinfo=0&modestbranding=1&playsinline=1",
            "price": 2.50, # currency 1.11
            "reviews": 1,
            "rating": 5.0,
            "shipping_fee": 5.49,
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

    def test_available_produkt_v2(self):
        url = "https://products.dm.de/product/DE/products/detail/gtin/4066447731538"
        body = None
        with open(
            "dm_test/jsons/produkt_4066447731538.json",
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
            "url": "https://www.dm.de/sportness-protein-wafer-bites-haselnuss-kakao-geschmack-p4066447731538.html",
            "source": "dm",
            "product_id": "1713565", # Artikelnummer意为商品号
            "existence": True,
            "title": "Protein Wafer Bites, Haselnuss-Kakao Geschmack, 30 g",
            # "description": None,
            "sku": "1713565",
            "upc": "4066447731538",
            "brand": "Sportness",
            "categories": 'Ernährung > Sportnahrung > Sport Zubehör & Spezialprodukte',
            "images": "https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1724664465/products/pim/4066447731538-1879991598/sportness-protein-wafer-bites-haselnuss-kakao-geschmack;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1724664465/products/pim/4066447731538-773503654/sportness-protein-wafer-bites-haselnuss-kakao-geschmack;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1724664465/products/pim/4066447731538-1281065010/sportness-protein-wafer-bites-haselnuss-kakao-geschmack",
            "videos": None,
            "price": 1.05, # currency 1.11
            "reviews": 30,
            "rating": 4.5,
            "shipping_fee": 5.49,
            "shipping_days_min": 2,
            "shipping_days_max": 3,
            "weight": 0.07, # kg -> lb 2.204623
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
            "weight",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])

    def test_available_produkt_v3(self):
        url = "https://products.dm.de/product/DE/products/detail/gtin/8700216386760"
        body = None
        with open(
            "dm_test/jsons/produkt_8700216386760.json",
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
            "url": "https://www.dm.de/oral-b-zahnseide-tiefenreinigung-gewachst-p8700216386760.html",
            "source": "dm",
            "product_id": "2477863", # Artikelnummer意为商品号
            "existence": True,
            "title": "Zahnseide Tiefenreinigung gewachst, 50 m",
            # "description": None,
            "sku": "2477863",
            "upc": "8700216386760",
            "brand": "Oral-B",
            "categories": 'Gesundheit > Zahnpflege > Interdentalbürsten & Zahnseide',
            "images": "https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1723164578/products/pim/8700216386760-1126492259/oral-b-zahnseide-tiefenreinigung-gewachst;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1723682786/products/pim/8700216386760-347327848/oral-b-zahnseide-tiefenreinigung-gewachst;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1723682786/products/pim/8700216386760-828959191/oral-b-zahnseide-tiefenreinigung-gewachst;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1723682786/products/pim/8700216386760-1432081877/oral-b-zahnseide-tiefenreinigung-gewachst;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1723682786/products/pim/8700216386760-980437479/oral-b-zahnseide-tiefenreinigung-gewachst;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1723682786/products/pim/8700216386760-497056032/oral-b-zahnseide-tiefenreinigung-gewachst;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1723682786/products/pim/8700216386760-843492273/oral-b-zahnseide-tiefenreinigung-gewachst;https://media.dm-static.com/images/f_auto,q_auto,c_fit,h_1200,w_1200/v1723682786/products/pim/8700216386760-493508149/oral-b-zahnseide-tiefenreinigung-gewachst",
            "videos": None,
            "price": 4.38, # currency 1.11
            "reviews": 0,
            "rating": 0.0,
            "shipping_fee": 5.49,
            "shipping_days_min": 2,
            "shipping_days_max": 3,
            "length": 1968.50, # cm -> inch 39.37008
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
            "length",
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])


if __name__ == "__main__":
    unittest.main()
