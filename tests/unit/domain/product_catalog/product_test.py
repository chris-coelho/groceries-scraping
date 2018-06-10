from unittest import TestCase

from src.domain.product_catalog.category import Category
from src.domain.product_catalog.product import Product
from src.domain.product_catalog.sub_category import SubCategory


class ProductTest(TestCase):
    def setUp(self):
        self.category = Category('Breads')
        self.sub_category = SubCategory('Gluten Free Breads', category=self.category)
        self.product = Product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                               gtin='1234567890123',
                               price=3.20,
                               sub_category=self.sub_category)
        self.product_with_id = Product(name='Warburtons Gluten Free Multiseed Loaf',
                                       gtin='1234567890321',
                                       price=3.20,
                                       sub_category=self.sub_category,
                                       _id='b07e1d28b7cf45deb63ff5f19e764f90')

    def test_create_product(self):
        self.assertIsNotNone(self.product)

    def test_create_product_with_id(self):
        self.assertIsNotNone(self.product_with_id)
        self.assertEqual(self.product_with_id.id, 'b07e1d28b7cf45deb63ff5f19e764f90')

    def test_product_as_json(self):
        expected = {
            'id': self.product.id,
            'name': 'Warburtons Gluten Free Tiger Artisan Bloomer',
            'gtin': '1234567890123',
            'price': 3.20,
            'sub_category': {
                'id': self.sub_category.id,
                'name': 'Gluten Free Breads'
            }
        }

        self.assertEqual(self.product.as_json(), expected)
