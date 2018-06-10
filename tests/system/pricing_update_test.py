from src.domain.pricing_updates.supermarket_vo import SupermarketVO
from src.domain.product_catalog.product import Product
from tests.base_test import BaseTest


class PricingUpdateTest(BaseTest):
    pass

    # def setUp(self):
    #     self.warburtons = Product(_id='dc29f65160de4ac6a30a4c526da02470',
    #                               name='Warburtons Gluten Free Tiger Artisan Bloomer',
    #                               gtin='1234567890111',
    #                               price=3.20,
    #                               sub_category=self.sub_category)
    #     self.my_supermarket = SupermarketVO(_id='e6981d6ea68b4cc682bbb03139ef679e',
    #                                         name='MySupermarket',
    #                                         is_active=True)
    #     self.sainsburys = SupermarketVO(_id='51264aa603ea49eeac59f26073999ede',
    #                                     name='Sainsburys',
    #                                     is_active=True)
    #     self.tesco = SupermarketVO(_id='91c5bb8d2ff54dce960ba7666ed9f9f4',
    #                                name='Tesco',
    #                                is_active=False)

    # def test_get_supermarkets_to_tracking(self):
    #     expected = [
    #         ProductSupermarket(self.warburtons, self.my_supermarket, 'http://www.mysupermarket.co.uk/warburtons'),
    #         ProductSupermarket(self.warburtons, self.sainsburys, 'http://www.sainsburys.co.uk/warburtons'),
    #     ]
    #
    #     self.assertListEqual(PricingUpdate().get_supermarkets_to_tracking(self.warburtons.id), expected)
    #
    # def test_activate_track(self):
    #     PricingUpdate().activate_track(product_id=self.warburtons.id,
    #                                    supermarket_id=self.my_supermarket.id,
    #                                    price_update_url='http://www.mysupermarket.co.uk/warburtons')
    #     product_supermarket = self.product_supermarket_repo.get_unique(product_id=self.warburtons.id,
    #                                                                    supermarket_id=self.my_supermarket.id)
    #     self.assertEqual(product_supermarket.is_active_tracking, True,
    #                      'The tracking should be active to {}'.format(product_supermarket.supermarket.name))
    #     self.assertEqual(product_supermarket.price_update_url, 'http://www.mysupermarket.co.uk/warburtons',
    #                      'The URL should be equal to {}'.format(product_supermarket.supermarket.name))
    #
    # def test_deactivate_track(self):
    #     PricingUpdate().deactivate_track(product_id=self.warburtons.id, supermarket_id=self.my_supermarket.id)
    #     product_supermarket = self.product_supermarket_repo.get_unique(product_id=self.warburtons.id,
    #                                                                    supermarket_id=self.my_supermarket.id)
    #     self.assertEqual(product_supermarket.is_active_tracking, False,
    #                      'The tracking should be inactive to {}'.format(product_supermarket.supermarket.name))

    # def tearDown(self):
    #     self.product_repo.delete(self.warburtons)
    #     self.supermarket_dao.delete(self.my_supermarket)
    #     self.supermarket_dao.delete(self.sainsburys)
    #     self.supermarket_dao.delete(self.tesco)
    #     for ps in self.product_supermarket_repo.get_all():
    #         self.product_supermarket_repo.delete(ps, False)
    #     self.product_supermarket_repo.commit()
