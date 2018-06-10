from unittest import TestCase

from src.domain.product_catalog.category import Category
from src.domain.product_catalog.category_guard import CategoryGuard


class CategoryGuardTest(TestCase):
    def test_check_ok(self):
        category = Category(name='Milk')
        self.assertTrue(CategoryGuard().check(category))

    def test_check_no_name(self):
        guard = CategoryGuard()
        null_name = Category(name=None)

        self.assertFalse(guard.check(null_name), 'No name is expected')

    def test_check_invalid_name(self):
        guard = CategoryGuard()
        short_name = Category(name='Mi')

        self.assertFalse(guard.check(short_name), 'A short name is expected.')
