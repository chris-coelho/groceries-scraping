from unittest import TestCase

from src.domain.product_catalog.category import Category


class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category('Milk')
        self.category_with_id = Category('Bread', _id='b07e1d28b7cf45deb63ff5f19e764f90')

    def test_create_category(self):
        self.assertIsNotNone(self.category)

    def test_create_category_with_id(self):
        self.assertIsNotNone(self.category_with_id)
        self.assertEqual(self.category_with_id.id, 'b07e1d28b7cf45deb63ff5f19e764f90')

    def test_category_as_json(self):
        expected = {
            'id': self.category.id,
            'name': 'Milk',
            'subcategories': []
        }
        self.assertEqual(self.category.as_json(), expected)
