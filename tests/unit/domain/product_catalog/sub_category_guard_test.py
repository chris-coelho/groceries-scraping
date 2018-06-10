from unittest import TestCase

from src.domain.product_catalog.category import Category
from src.domain.product_catalog.sub_category import SubCategory
from src.domain.product_catalog.sub_category_guard import SubCategoryGuard


class SubCategoryGuardTest(TestCase):

    def test_check_ok(self):
        sub_category = SubCategory(name='Milks',
                                   category=Category('Milk'))
        self.assertTrue(SubCategoryGuard().check(sub_category))

    def test_check_no_name(self):
        guard = SubCategoryGuard()
        null_name = SubCategory(name=None,
                                category=Category('Milk'))

        self.assertFalse(guard.check(null_name), 'No name is expected')

    def test_check_invalid_name(self):
        guard = SubCategoryGuard()
        short_name = SubCategory(name='Mi',
                                 category=Category('Milk'))

        self.assertFalse(guard.check(short_name), 'A short name is expected.')

    def test_check_invalid_category(self):
        guard = SubCategoryGuard()
        invalid_category = SubCategory(name='Milk', category=None)

        self.assertFalse(guard.check(invalid_category), 'No category is expected.')
