import unittest
from scrapy.utils.test import get_crawler
from scrapy.http import Request, Response, HtmlResponse
from greenist.spiders.docmorris import DocMorrisSpider


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.crawler = get_crawler(DocMorrisSpider)
        self.spider = self.crawler._create_spider()

    def test_available_produkt_v1(self):
        url = "https://www.docmorris.de/docmorris-vitamin-d3-tabletten-800-ie/08068486"
        body = None
        with open(
            "docmorris_test/htmls/docmorris-vitamin-d3-tabletten-800-ie_08068486.html",
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
            "url": "https://www.docmorris.de/docmorris-vitamin-d3-tabletten-800-ie/08068486",
            "source": "DrMorris",
            "product_id": "b807667a-b87d-40a7-ad50-0eb4aed4e0b1",
            "existence": True,
            "title": "DocMorris Vitamin D3 Tabletten 800 I.E. 60 St",
            # "description": None,
            "sku": "7YTK1Z5G", # SKU通常为8位
            "upc": "08068486",
            "brand": None,
            "categories": 'Vitamine, Sport & Ernährung > Vitamine & Mineralstoffe > Vitamine > Vitamin D',
            "images": "https://statics.docmorris.de/static/produkte/7YTK1Z5G/docmorris/ps420r/docmorris-vitamin-d3-tabletten-800-i-e-60-st-08068486-0-1714032136152762.jpeg;https://statics.docmorris.de/static/produkte/7YTK1Z5G/docmorris/ps420r/docmorris-vitamin-d3-tabletten-800-i-e-60-st-08068486-front-1714032135798240.jpeg;https://statics.docmorris.de/static/produkte/7YTK1Z5G/docmorris/ps420r/docmorris-vitamin-d3-tabletten-800-i-e-60-st-08068486-back-1714032135457247.jpeg;https://statics.docmorris.de/static/produkte/7YTK1Z5G/docmorris/ps420r/docmorris-vitamin-d3-tabletten-800-i-e-60-st-08068486-left-1714032135849092.jpeg;https://statics.docmorris.de/static/produkte/7YTK1Z5G/docmorris/ps420r/docmorris-vitamin-d3-tabletten-800-i-e-60-st-08068486-right-1714032136126479.jpeg",
            "price": 3.32, # currency 1.11
            "reviews": 0,
            "rating": None,
            "shipping_fee": 3.89,
            "shipping_days_min": 0,
            "shipping_days_max": 1,
        }

        keys = [
            "url",
            "source",
            "product_id",
            "readable_id",
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
        url = "https://www.docmorris.de/kytta-schmerzsalbe/10832865"
        body = None
        with open(
            "docmorris_test/htmls/kytta-schmerzsalbe_10832865.html",
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
            "url": "https://www.docmorris.de/kytta-schmerzsalbe/10832865",
            "source": "DocMorris",
            "product_id": "722c92b9-f4ba-4ffb-8bad-efdda3d39171",
            "existence": True,
            "title": "Kytta Schmerzsalbe 150 g",
            # "description": None,
            "sku": "FX5UP389",
            "upc": "10832865",
            "brand": "Kytta",
            "categories": 'Arzneimittel & Gesundheit > Muskeln, Knochen, Gelenke > Stauchung, Prellung & Zerrung > Cremes & Gele',
            "images": "https://statics.docmorris.de/static/produkte/FX5UP389/docmorris/ps420r/kytta-schmerzsalbe-150-g-10832865-0-1720620118087441.jpg;https://statics.docmorris.de/static/produkte/FX5UP389/docmorris/ps420r/kytta-schmerzsalbe-150-g-10832865-2-1720620118721051.jpeg;https://statics.docmorris.de/static/produkte/FX5UP389/docmorris/ps420r/kytta-schmerzsalbe-150-g-10832865-3-1720620118989838.jpeg;https://statics.docmorris.de/static/produkte/FX5UP389/docmorris/ps420r/kytta-schmerzsalbe-150-g-10832865-4-1720620119264784.jpeg;https://statics.docmorris.de/static/produkte/FX5UP389/docmorris/ps420r/kytta-schmerzsalbe-150-g-10832865-5-1720620119632811.jpeg;https://statics.docmorris.de/static/produkte/FX5UP389/docmorris/ps420r/kytta-schmerzsalbe-150-g-10832865-6-1720620119915471.jpeg;https://statics.docmorris.de/static/produkte/FX5UP389/docmorris/ps420r/kytta-schmerzsalbe-150-g-10832865-7-1720620120183847.jpeg",
            "videos": None,
            "price": 21.08, # currency 1.11
            "reviews": 495,
            "rating": 4.6,
            "shipping_fee": 3.89,
            "shipping_days_min": 0,
            "shipping_days_max": 1,
            "weight": 0.33, # kg -> lb 2.204623
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
        url = "https://www.docmorris.de/thermometer-10100-c-20-cm-lang/15656657"
        body = None
        with open(
            "docmorris_test/htmls/thermometer-10100-c-20-cm-lang_15656657.html",
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
            "url": "https://www.docmorris.de/thermometer-10100-c-20-cm-lang/15656657",
            "source": "DocMorris",
            "product_id": "33286c28-f941-455c-8eae-b29bb4ddfe7e",
            "existence": True,
            "title": "Thermometer 10-100° C 20 cm lang 1 St",
            # "description": None,
            "sku": "FX5AG5Z3",
            "upc": "15656657",
            "brand": None,
            "categories": 'Arzneimittel & Gesundheit > Haus- & Reiseapotheke > Hausapotheke > Erste Hilfe & Verbandmittel',
            "images": "https://statics.docmorris.de/static/produkte/FX5AG5Z3/docmorris/ps420r/thermometer-10-1000-c-20-cm-lang-1-st-15656657-default-1714050672913044.jpeg",
            "videos": None,
            "price": 5.87, # currency 1.11
            "reviews": 1,
            "rating": 5.0,
            "shipping_fee": 3.89,
            "shipping_days_min": 0,
            "shipping_days_max": 1,
            "length": 7.87, # cm -> in 0.393701
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

    def test_available_produkt_v4(self):
        url = "https://www.docmorris.de/eskompressen-steril-8f-10-x-20-cm/01407092"
        body = None
        with open(
            "docmorris_test/htmls/eskompressen-steril-8f-10-x-20-cm_01407092.html",
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
            "url": "https://www.docmorris.de/eskompressen-steril-8f-10-x-20-cm/01407092",
            "source": "DocMorris",
            "product_id": "6e3b2311-0250-4002-b135-a2234b227ff6",
            "existence": True,
            "title": "ES-Kompressen steril 8f 10 x 20 cm 25X2 St",
            # "description": None,
            "sku": "LG1G161S",
            "upc": "01407092",
            "brand": None,
            "categories": 'Arzneimittel & Gesundheit > Haus- & Reiseapotheke > Hausapotheke > Erste Hilfe & Verbandmittel',
            "images": "https://statics.docmorris.de/static/produkte/FX5AG5Z3/docmorris/ps420r/thermometer-10-1000-c-20-cm-lang-1-st-15656657-default-1714050672913044.jpeg",
            "videos": None,
            "price": 28.29, # currency 1.11
            "reviews": 1,
            "rating": 5.0,
            "shipping_fee": 0.00,
            "shipping_days_min": 0,
            "shipping_days_max": 1,
            "weight": 0.44,
            "width": 3.94, # cm -> in 0.393701
            "length": 7.87
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
            "width",
            "length"
        ]
        for key in keys:
            self.assertEqual(product[key], target_product[key])

    def test_unavailable_produkt(self):
        url = "https://www.docmorris.de/hitzer-loesung/04982721"
        body = None
        with open(
            "dm_test/htmls/hitzer-loesung_04982721.html",
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
            "url": "https://www.docmorris.de/hitzer-loesung/04982721",
            "source": "DocMorris",
            "product_id": "fe6912e5-4006-4e64-bc21-61f60569591e",
            "existence": False,
            "title": "Hitzer Lösung 30 ml",
            # "description": None,
            "sku": "FX5RAAYX",
            "upc": "04982721",
            "brand": None,
            "categories": None,
            "images": "https://statics.docmorris.de/static/docmorris/cms/ps420r/docmorris_fallback_6a098c8404.jpeg",
            "videos": None,
            "price": 33.68, # currency 1.11
            "available_qty": 0,
            "reviews": 0,
            "rating": None,
            "shipping_fee": 0.00,
            "shipping_days_min": 0,
            "shipping_days_max": 1,
            "weight": 0.07
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
