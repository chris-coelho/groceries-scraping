from unittest import TestCase, mock

from src.domain.product_catalog.category import Category
from src.domain.product_catalog.product import Product
from src.domain.product_catalog.product_factory import ProductFactory
from src.domain.product_catalog.sub_category import SubCategory


class ProductFactoryTest(TestCase):
    def setUp(self):
        self.category_repo = mock.Mock()
        self.sub_category_repo = mock.Mock()
        self.product_repo = mock.Mock()
        self.product_factory = ProductFactory(category_repo=self.category_repo,
                                              sub_category_repo=self.sub_category_repo,
                                              product_repo=self.product_repo)

    def test_default_category_with(self):
        category = self.product_factory.default_category_with('Milks')
        self.assertIsNotNone(category)

    def test_default_category_to_update(self):
        self.category_repo.get_by_id.return_value = Category(_id='418f5f846e1149e28b5f5310bc7ea8c5',
                                                             name='Milks')
        category = self.product_factory.default_category_to_update(_id='418f5f846e1149e28b5f5310bc7ea8c5',
                                                                   name='Good Milks')

        self.assertIsNotNone(category)
        self.assertEqual(category.name, 'Good Milks')

    def test_default_sub_category_with(self):
        self.category_repo.get_by_id.return_value = Category(_id='418f5f846e1149e28b5f5310bc7ea8c5',
                                                             name='Breads')
        sub_category = self.product_factory.default_sub_category_with(name='White Breads',
                                                                      category_id='418f5f846e1149e28b5f5310bc7ea8c5')
        self.assertIsNotNone(sub_category)

    def test_default_sub_category_to_update(self):
        category = Category(_id='418f5f846e1149e28b5f5310bc7ea8c5', name='Breads')
        self.category_repo.get_by_id.return_value = category
        self.sub_category_repo.get_by_id.return_value = SubCategory(_id='b07e1d28b7cf45deb63ff5f19e764f90',
                                                                    name='White Breads',
                                                                    category=category)
        sub_category = self.product_factory.default_sub_category_to_update(_id='b07e1d28b7cf45deb63ff5f19e764f90',
                                                                           name='Gluten Free Breads',
                                                                           category_id=category.id)
        self.assertIsNotNone(sub_category)
        self.assertEqual(sub_category.name, 'Gluten Free Breads')

    def test_default_product_with(self):
        category = Category(_id='418f5f846e1149e28b5f5310bc7ea8c5', name='Breads')
        sub_category = SubCategory(_id='b07e1d28b7cf45deb63ff5f19e764f90', name='White Breads', category=category)
        self.sub_category_repo.get_by_id.return_value = sub_category
        self.product_repo.get_by_gtin.return_value = None

        product = self.product_factory.default_product_with(name='Warburtons Gluten Free Multiseed Loaf',
                                                            gtin='1234567890123',
                                                            price=5.99,
                                                            sub_category_id=sub_category.id)

        self.assertIsNotNone(product)

    def test_default_product_to_update(self):
        category = Category(_id='418f5f846e1149e28b5f5310bc7ea8c5', name='Breads')
        sub_category = SubCategory(_id='b07e1d28b7cf45deb63ff5f19e764f90', name='White Breads', category=category)
        self.sub_category_repo.get_by_id.return_value = sub_category
        self.product_repo.get_by_id.return_value = Product(name='Warburtons Gluten Free Multiseed Loaf',
                                                           gtin='1234567890123',
                                                           price=5.99,
                                                           sub_category=sub_category)

        product = self.product_factory.default_product_to_update(name='Warburtons Gluten Free Multiseed Loaf',
                                                                 gtin='1234567890123',
                                                                 price=7.99,
                                                                 sub_category_id=sub_category.id,
                                                                 _id='6fc9713877dc40f78ba5f77136c6c67b')

        self.assertIsNotNone(product)
        self.assertEqual(product.price, 7.99)
