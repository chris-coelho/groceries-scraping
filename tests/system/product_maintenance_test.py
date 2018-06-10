from src.application.product_maintenance import ProductMaintenance
from src.domain.product_catalog.product import Product
from tests.system.base_test import BaseTest


class ProductMaintenanceTest(BaseTest):

    def setUp(self):
        self.products = [
            Product(_id='ff8232c3c9b34b5db7838967ac9ddfa4',
                    name='Warburtons Gluten Free Tiger Artisan Bloomer',
                    gtin='1234567890123',
                    price=3.20,
                    sub_category=self.sub_category),
            Product(_id='3d4db78b23ac4e72b6e6b5fc10f3802e',
                    name='ASDA Soft White Toastie Thick Sliced Bread 800g',
                    gtin='1234567890321',
                    price=5.90,
                    sub_category=self.sub_category)
        ]
        self.product_maintenance = ProductMaintenance()

    def test_create_product(self):
        self.product_maintenance.create_product(name=self.products[0].name,
                                                gtin=self.products[0].gtin,
                                                price=self.products[0].price,
                                                sub_category_id=self.sub_category.id)

        product = self.product_repo.get_by_gtin(self.products[0].gtin)

        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'Warburtons Gluten Free Tiger Artisan Bloomer')
        self.assertEqual(product.price, 3.20)

    def test_get_product(self):
        for product in self.products:
            self.product_maintenance.create_product(name=product.name,
                                                    gtin=product.gtin,
                                                    price=product.price,
                                                    sub_category_id=self.sub_category.id)

        product = self.product_maintenance.get_product(self.products[1].id)

        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'ASDA Soft White Toastie Thick Sliced Bread 800g')

    def test_get_products_list(self):
        for product in self.products:
            self.product_maintenance.create_product(name=product.name,
                                                    gtin=product.gtin,
                                                    price=product.price,
                                                    sub_category_id=self.sub_category.id)

        products = self.product_maintenance.get_products_list()

        self.assertIsNotNone(products)
        self.assertEqual(len(products), 2)

    def tearDown(self):
        self.product_repo.delete(self.product_repo.get_by_gtin('1234567890123'))
        self.product_repo.delete(self.product_repo.get_by_gtin('1234567890321'))
