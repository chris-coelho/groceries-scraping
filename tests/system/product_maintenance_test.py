from src.application.product_maintenance import ProductMaintenance
from tests.base_test import BaseTest


class ProductMaintenanceTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.product_maintenance = ProductMaintenance()

    def test_create_product(self):
        with self.app_context():
            self.product_maintenance.create_product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                                                    gtin='0234567890000',
                                                    price=3.20,
                                                    sub_category_id=self.sub_category.id)

            product = self.product_repo.get_by_gtin('0234567890000')

            self.assertIsNotNone(product)
            self.assertEqual(product.name, 'Warburtons Gluten Free Tiger Artisan Bloomer')
            self.assertEqual(product.price, 3.20)

    def test_get_product(self):
        with self.app_context():
            warburtons = self.product_maintenance.create_product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                                                                 gtin='0234567890000',
                                                                 price=3.20,
                                                                 sub_category_id=self.sub_category.id)
            asda_toast = self.product_maintenance.create_product(name='ASDA Soft White Toastie Thick Sliced Bread 800g',
                                                                 gtin='2234567890222',
                                                                 price=5.90,
                                                                 sub_category_id=self.sub_category.id)

            product = self.product_maintenance.get_product(asda_toast.id)

            self.assertIsNotNone(product)
            self.assertEqual(product.name, 'ASDA Soft White Toastie Thick Sliced Bread 800g')

    def test_get_products_list(self):
        with self.app_context():
            warburtons = self.product_maintenance.create_product(name='Warburtons Gluten Free Tiger Artisan Bloomer',
                                                                 gtin='0234567890000',
                                                                 price=3.20,
                                                                 sub_category_id=self.sub_category.id)
            asda_toast = self.product_maintenance.create_product(name='ASDA Soft White Toastie Thick Sliced Bread 800g',
                                                                 gtin='2234567890222',
                                                                 price=5.90,
                                                                 sub_category_id=self.sub_category.id)

            products = self.product_maintenance.get_products_list()

            self.assertIsNotNone(products)
            self.assertEqual(len(products), 2)
            self.assertEqual(products[0].gtin, warburtons.gtin)
            self.assertEqual(products[1].price, asda_toast.price)
