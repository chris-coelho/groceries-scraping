from unittest import TestCase

from src.domain.pricing_updates.product_supermarket import ProductSupermarket
from src.domain.pricing_updates.product_supermarket_guard import ProductSupermarketGuard
from src.domain.pricing_updates.supermarket_vo import SupermarketVO
from src.domain.product_catalog.category import Category
from src.domain.product_catalog.product import Product
from src.domain.product_catalog.sub_category import SubCategory


class ProductSupermarketGuardTest(TestCase):
    def setUp(self):
        self.category = Category('Breads')
        self.sub_category = SubCategory('Gluten Free Breads', category=self.category)
        self.product = Product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                               gtin='1234567890123',
                               price=3.20,
                               sub_category=self.sub_category)
        self.supermarket = SupermarketVO(_id='e6981d6ea68b4cc682bbb03139ef679e',
                                         name='MySupermarket',
                                         is_active=True)

    def test_check_ok(self):
        product_supermarket = ProductSupermarket(product=self.product,
                                                 supermarket=self.supermarket,
                                                 price_update_url='http://www.mysupermarket.co.uk')
        self.assertTrue(ProductSupermarketGuard().check(product_supermarket))

    def test_check_no_product(self):
        guard = ProductSupermarketGuard()
        product_supermarket = ProductSupermarket(product=None,
                                                 supermarket=self.supermarket,
                                                 price_update_url='http://www.mysupermarket.co.uk')

        self.assertFalse(guard.check(product_supermarket), 'No product is expected')

    def test_check_no_supermarket(self):
        guard = ProductSupermarketGuard()
        product_supermarket = ProductSupermarket(product=self.product,
                                                 supermarket=None,
                                                 price_update_url='http://www.mysupermarket.co.uk')

        self.assertFalse(guard.check(product_supermarket), 'No supermarket is expected')

    def test_check_no_url(self):
        guard = ProductSupermarketGuard()
        product_supermarket = ProductSupermarket(product=self.product,
                                                 supermarket=self.supermarket,
                                                 price_update_url=None)

        self.assertFalse(guard.check(product_supermarket), 'No URL is expected')

