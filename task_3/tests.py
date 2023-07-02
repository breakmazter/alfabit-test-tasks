from django.test import TestCase

from task_3.models import Product


class ProductBuyTestCase(TestCase):
    @staticmethod
    def test_product_buy() -> None:
        Product.buy(user='iosif', item_id='1')
