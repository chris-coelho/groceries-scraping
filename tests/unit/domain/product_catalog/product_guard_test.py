from unittest import TestCase

from src.domain.product_catalog.category import Category
from src.domain.product_catalog.product import Product
from src.domain.product_catalog.product_guard import ProductGuard
from src.domain.product_catalog.sub_category import SubCategory


class ProductGuardTest(TestCase):
    def setUp(self):
        self.category = Category('Breads')
        self.sub_category = SubCategory('Gluten Free Breads', category=self.category)

    def test_check_ok(self):
        product = Product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                          gtin='1234567890123',
                          price=3.20,
                          sub_category=self.sub_category)

        self.assertTrue(ProductGuard().check(product))

    def test_check_no_name(self):
        product = Product(name=None,
                          gtin='1234567890123',
                          price=3.20,
                          sub_category=self.sub_category)

        self.assertFalse(ProductGuard().check(product), 'Name not expected.')

    def test_check_invalid_name(self):
        product = Product(name='Wa',
                          gtin='1234567890123',
                          price=3.20,
                          sub_category=self.sub_category)

        self.assertFalse(ProductGuard().check(product), 'A short name is expected')

    def test_check_no_gtin(self):
        product = Product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                          gtin=None,
                          price=3.20,
                          sub_category=self.sub_category)

        self.assertFalse(ProductGuard().check(product), 'No GTIN expected')

    def test_check_invalid_gtin(self):
        less_than_13 = Product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                               gtin='123456789012',
                               price=3.20,
                               sub_category=self.sub_category)
        greater_than_13 = Product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                                  gtin='12345678901234',
                                  price=3.20,
                                  sub_category=self.sub_category)

        self.assertFalse(ProductGuard().check(less_than_13), 'GTIN less than 13 characters expected.')
        self.assertFalse(ProductGuard().check(greater_than_13), 'GTIN greater than 13 characters expected.')

    def test_check_invalid_price(self):
        no_price = Product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                           gtin='1234567890123',
                           price=0,
                           sub_category=self.sub_category)
        greater_then_one_million = Product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                                           gtin='1234567890123',
                                           price=1000001,
                                           sub_category=self.sub_category)

        self.assertFalse(ProductGuard().check(no_price), 'No price expected.')
        self.assertFalse(ProductGuard().check(greater_then_one_million), 'Price greater than 1 million expected.')

    def test_check_invalid_category(self):
        no_category = Product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                              gtin='1234567890123',
                              price=3.20,
                              sub_category=None)

        self.assertFalse(ProductGuard().check(no_category), 'No category expected.')
