from src.domain.product_catalog.category import Category
from src.domain.product_catalog.category_guard import CategoryGuard
from src.domain.product_catalog.product import Product
from src.domain.product_catalog.product_guard import ProductGuard
from src.domain.product_catalog.sub_category import SubCategory
from src.domain.product_catalog.sub_category_guard import SubCategoryGuard
from src.domain.validations.gtin_should_be_unique_validation import gtin_should_be_unique_validation
from src.infra.cross_cutting.exceptions.category_exceptions import CategoryException, CategoryNotFoundException
from src.infra.cross_cutting.exceptions.product_exceptions import ProductRequiresSubCategoryException, ProductException, \
    ProductNotFoundException, ProductWithDuplicatedGtinException
from src.infra.cross_cutting.exceptions.sub_category_exceptions import CategoryRequiredException, \
    SubCategoryNotFoundException


class ProductFactory:
    def __init__(self,
                 category_repo,
                 sub_category_repo,
                 product_repo):
        self.__category_repo = category_repo
        self.__sub_category_repo = sub_category_repo
        self.__product_repo = product_repo

    def default_category_with(self, name):
        category = Category(name=name)
        guard = CategoryGuard()
        if not guard.check(category):
            raise CategoryException(guard.get_issues())

        return category

    def default_category_to_update(self, _id, name):
        category = self.__category_repo.get_by_id(_id)
        if not category:
            raise CategoryNotFoundException(_id)

        category.name = name

        guard = CategoryGuard()
        if not guard.check(category):
            raise CategoryException(guard.get_issues())

        return category

    def default_sub_category_with(self, name, category_id):
        category = self.__category_repo.get_by_id(category_id)
        if not category:
            raise CategoryRequiredException(category_id)

        sub_category = SubCategory(name=name, category=category)
        guard = SubCategoryGuard()
        if not guard.check(sub_category):
            raise CategoryException(guard.get_issues())

        return sub_category

    def default_sub_category_to_update(self, _id, name, category_id):
        category = self.__category_repo.get_by_id(category_id)
        if not category:
            raise CategoryRequiredException(category_id)

        sub_category = self.__sub_category_repo.get_by_id(_id)
        if not sub_category:
            raise SubCategoryNotFoundException(_id)

        sub_category.name = name
        sub_category.category = category

        guard = SubCategoryGuard()
        if not guard.check(sub_category):
            raise CategoryException(guard.get_issues())

        return sub_category

    def default_product_with(self, name, gtin, price, sub_category_id):
        sub_category = self.__sub_category_repo.get_by_id(sub_category_id)
        if not sub_category:
            raise ProductRequiresSubCategoryException(sub_category_id)

        # if not gtin_should_be_unique_validation(self.__product_repo, gtin):
        #     raise ProductWithDuplicatedGtinException(gtin)

        product = Product(name=name, gtin=gtin, price=price, sub_category=sub_category)

        guard = ProductGuard()
        if not guard.check(product):
            raise ProductException(guard.get_issues())

        return product

    def default_product_to_update(self, _id, name, gtin, price, sub_category_id):
        sub_category = self.__sub_category_repo.get_by_id(sub_category_id)
        if not sub_category:
            raise ProductRequiresSubCategoryException(sub_category_id)

        product = self.__product_repo.get_by_id(_id)
        if not product:
            raise ProductNotFoundException(_id)

        if gtin != product.gtin:
            if not gtin_should_be_unique_validation(self.__product_repo, gtin):
                raise ProductWithDuplicatedGtinException(gtin)

        product.name = name
        product.gtin = gtin
        product.price = price
        product.sub_category = sub_category

        guard = ProductGuard()
        if not guard.check(product):
            raise ProductException(guard.get_issues())

        return product

