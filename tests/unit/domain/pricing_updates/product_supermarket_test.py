from unittest import TestCase

from src.domain.pricing_updates.product_supermarket import ProductSupermarket
from src.domain.pricing_updates.supermarket_vo import SupermarketVO
from src.domain.product_catalog.category import Category
from src.domain.product_catalog.product import Product
from src.domain.product_catalog.sub_category import SubCategory


class ProductSupermarketTest(TestCase):
    def setUp(self):
        self.category = Category('Breads')
        self.sub_category = SubCategory('Gluten Free Breads', category=self.category)
        product = Product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                          gtin='1234567890123',
                          price=3.20,
                          sub_category=self.sub_category)
        supermarket = SupermarketVO(_id='e6981d6ea68b4cc682bbb03139ef679e',
                                    name='MySupermarket',
                                    is_active=True)
        self.product_supermarket = ProductSupermarket(product=product,
                                                      supermarket=supermarket,
                                                      price_update_url='http://www.mysupermarket.co.uk')
        self.product_supermarket_with_id = ProductSupermarket(product=product,
                                                              supermarket=supermarket,
                                                              price_update_url='http://www.mysupermarket.co.uk',
                                                              _id='fdf88acb94984a859bd342c05ead9beb')

    def test_create_product_supermarket(self):
        self.assertIsNotNone(self.product_supermarket)

    def test_create_product_supermarket_with_id(self):
        self.assertIsNotNone(self.product_supermarket_with_id)
        self.assertEqual(self.product_supermarket_with_id.id, 'fdf88acb94984a859bd342c05ead9beb')

    def test_product_supermarket_as_json(self):
        expected = {
            'id': self.product_supermarket.id,
            'price_update_url': 'http://www.mysupermarket.co.uk',
            'is_active_tracking': False,
            'current_price': 0,
            'last_update': None,
            'product': {
                'id': self.product_supermarket.product.id,
                'name': 'Warburtons Gluten Free Tiger Artisan Bloomer'
            },
            'supermarket': {
                'id': self.product_supermarket.supermarket.id,
                'name': 'MySupermarket'
            },
        }
        self.assertEqual(self.product_supermarket.as_json(), expected)
