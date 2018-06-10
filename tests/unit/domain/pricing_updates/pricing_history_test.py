from datetime import datetime
from unittest import TestCase

from src.domain.pricing_updates.pricing_history import PricingHistory


class PricingHistoryTest(TestCase):
    def setUp(self):
        self.now = datetime.now()
        self.pricing_history = PricingHistory(product_supermarket_id='b2151d902f1048b69cf7203f92bc9e48',
                                              price=5.29,
                                              update_on=self.now)
        self.pricing_history_with_id = PricingHistory(product_supermarket_id='b2151d902f1048b69cf7203f92bc9e48',
                                                      price=5.29,
                                                      update_on=self.now,
                                                      _id='d44a36da42ef47f68b22c87bdf2e125a')

    def test_create_pricing_history(self):
        self.assertIsNotNone(self.pricing_history)

    def test_create_pricing_history_with_id(self):
        self.assertIsNotNone(self.pricing_history_with_id)
        self.assertEqual(self.pricing_history_with_id.id, 'd44a36da42ef47f68b22c87bdf2e125a')

    def test_pricing_history_as_json(self):
        expected = {
            'id': self.pricing_history.id,
            'product_supermarket_id': 'b2151d902f1048b69cf7203f92bc9e48',
            'price': 5.29,
            'update_on': self.now.strftime('%Y-%m-%d %H:%M:%S')
        }
        self.assertEqual(self.pricing_history.as_json(), expected)
