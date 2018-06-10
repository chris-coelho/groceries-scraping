from unittest import TestCase

from src.domain.product_catalog.category import Category
from src.domain.product_catalog.sub_category import SubCategory


class SubCategoryTest(TestCase):
    def setUp(self):
        self.sub_category = SubCategory('Milks',
                                        Category('Milk'))
        self.sub_category_with_id = SubCategory('White Breads',
                                                Category('Bread'),
                                                _id='b07e1d28b7cf45deb63ff5f19e764f90')

    def test_create_sub_category(self):
        self.assertIsNotNone(self.sub_category)

    def test_create_sub_category_with_id(self):
        self.assertIsNotNone(self.sub_category_with_id)
        self.assertEqual(self.sub_category_with_id.id, 'b07e1d28b7cf45deb63ff5f19e764f90')

    def test_sub_category_as_json(self):
        expected = {
            'id': self.sub_category.id,
            'name': 'Milks',
            'category': {
                'id': self.sub_category.category.id,
                'name': 'Milk'
            },
            'products': []
        }
        self.assertEqual(self.sub_category.as_json(), expected)


