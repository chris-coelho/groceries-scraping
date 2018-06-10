from unittest import TestCase

from src.domain.pricing_updates.supermarket_vo import SupermarketVO


class SupermarketVOTest(TestCase):
    def setUp(self):
        self.supermarket = SupermarketVO(_id='a04223097d4c4166a77475b2e25b0ef0',
                                         name='MySupermarket',
                                         is_active=True)

    def test_create_supermarket(self):
        self.assertIsNotNone(self.supermarket)
        self.assertEqual(self.supermarket.id, 'a04223097d4c4166a77475b2e25b0ef0')
        self.assertEqual(self.supermarket.name, 'MySupermarket')
        self.assertEqual(self.supermarket.is_active, True)

    def test_supermarket_as_json(self):
        expected = {
            'id': 'a04223097d4c4166a77475b2e25b0ef0',
            'name': 'MySupermarket',
            'is_active': True,
            'module_name': None,
            'class_name': None
        }
        self.assertEqual(self.supermarket.as_json(), expected)
