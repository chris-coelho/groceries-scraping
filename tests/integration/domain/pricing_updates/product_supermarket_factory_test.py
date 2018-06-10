from unittest import TestCase, mock

from src.domain.pricing_updates.boa_scraping import BoaScraping
from src.domain.pricing_updates.carrefour_scraping import CarrefourScraping
from src.domain.pricing_updates.product_supermarket import ProductSupermarket
from src.domain.pricing_updates.product_supermarket_factory import ProductSupermarketFactory
from src.domain.pricing_updates.supermarket_vo import SupermarketVO
from src.domain.product_catalog.category import Category
from src.domain.product_catalog.product import Product
from src.domain.product_catalog.sub_category import SubCategory


class ProductSupermarketFactoryTest(TestCase):
    def setUp(self):
        self.product_repo = mock.Mock()
        self.supermarket_dao = mock.Mock()
        self.product_supermarket_repo = mock.Mock()
        self.product_supermarket_factory = ProductSupermarketFactory(self.product_repo,
                                                                     self.supermarket_dao,
                                                                     self.product_supermarket_repo)
        self.category = Category('Breads')
        self.sub_category = SubCategory('Gluten Free Breads', category=self.category)
        self.product = Product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                               gtin='1234567890123',
                               price=3.20,
                               sub_category=self.sub_category)
        self.supermarket = SupermarketVO(_id='e6981d6ea68b4cc682bbb03139ef679e',
                                         name='MySupermarket',
                                         is_active=True)
        self.existing_product_supermarket = ProductSupermarket(product=self.product,
                                                               supermarket=self.supermarket,
                                                               price_update_url='http://www.mysupermarket.co.uk')

    def test_activate_tracking(self):
        self.product_repo.get_by_id.return_value = self.product
        self.supermarket_dao.get_by_id.return_value = self.supermarket
        self.product_supermarket_repo.get_unique.return_value = self.existing_product_supermarket

        product_supermarket = self.product_supermarket_factory.activate_tracking(product_id=self.product.id,
                                                                                 supermarket_id=self.supermarket.id,
                                                                                 price_update_url='http://www.mysupermarket.co.uk')

        self.assertIsNotNone(product_supermarket)
        self.assertEqual(product_supermarket.is_active_tracking, True)

    def test_deactivate_tracking(self):
        self.product_repo.get_by_id.return_value = self.product
        self.supermarket_dao.get_by_id.return_value = self.supermarket
        self.product_supermarket_repo.get_unique.return_value = self.existing_product_supermarket

        product_supermarket = self.product_supermarket_factory.deactivate_tracking(product_id=self.product.id,
                                                                                   supermarket_id=self.supermarket.id)

        self.assertIsNotNone(product_supermarket)
        self.assertEqual(product_supermarket.is_active_tracking, False)

    def test_product_for_price_update_to_boa(self):
        self.product_supermarket_repo.get_by_id.return_value = self.existing_product_supermarket
        boa = self.supermarket
        boa.module_name = 'src.domain.pricing_updates.boa_scraping'
        boa.class_name = 'BoaScraping'
        self.existing_product_supermarket.is_active_tracking = True
        product_supermarket = self.product_supermarket_factory.\
            product_for_price_update(self.existing_product_supermarket.id)

        self.assertIsNotNone(product_supermarket)
        self.assertIsInstance(product_supermarket.web_scraping, BoaScraping)

    def test_product_for_price_update_to_carrefour(self):
        self.product_supermarket_repo.get_by_id.return_value = self.existing_product_supermarket
        boa = self.supermarket
        boa.module_name = 'src.domain.pricing_updates.carrefour_scraping'
        boa.class_name = 'CarrefourScraping'
        self.existing_product_supermarket.is_active_tracking = True
        product_supermarket = self.product_supermarket_factory.\
            product_for_price_update(self.existing_product_supermarket.id)

        self.assertIsNotNone(product_supermarket)
        self.assertIsInstance(product_supermarket.web_scraping, CarrefourScraping)
