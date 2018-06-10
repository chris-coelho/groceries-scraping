import importlib

from src.domain.pricing_updates.product_supermarket import ProductSupermarket
from src.domain.pricing_updates.product_supermarket_guard import ProductSupermarketGuard
from src.infra.cross_cutting.exceptions.product_exceptions import ProductNotFoundException
from src.infra.cross_cutting.exceptions.product_supermarket_exceptions import ProductSupermarketException
from src.infra.cross_cutting.exceptions.supermarket_exceptions import SupermarketNotFoundException
from src.infra.cross_cutting.http_requests_util import HttpRequestsUtil


class ProductSupermarketFactory:
    def __init__(self,
                 product_repo,
                 supermarket_dao,
                 product_supermarket_repo):
        self.__product_repo = product_repo
        self.__supermarket_dao = supermarket_dao
        self.__product_supermarket_repo = product_supermarket_repo

    def activate_tracking(self, product_id, supermarket_id, price_update_url):
        product = self.__get_product(product_id)
        supermarket = self.__get_supermarket(supermarket_id)

        product_supermarket = self.__product_supermarket_repo.get_unique(product_id, supermarket_id)
        if product_supermarket:
            product_supermarket.price_update_url = price_update_url
        else:
            product_supermarket = self.__new_product_supermarket(product=product,
                                                                 supermarket=supermarket,
                                                                 price_update_url=price_update_url)

        product_supermarket.is_active_tracking = True

        guard = ProductSupermarketGuard()
        if not guard.check(product_supermarket):
            raise ProductSupermarketException(guard.get_issues())

        return product_supermarket

    def deactivate_tracking(self, product_id, supermarket_id):
        product = self.__get_product(product_id)
        supermarket = self.__get_supermarket(supermarket_id)

        product_supermarket = self.__product_supermarket_repo.get_unique(product_id, supermarket_id)
        if not product_supermarket:
            product_supermarket = self.__new_product_supermarket(product=product,
                                                                 supermarket=supermarket,
                                                                 price_update_url='http://')

        product_supermarket.is_active_tracking = False

        guard = ProductSupermarketGuard()
        if not guard.check(product_supermarket):
            raise ProductSupermarketException(guard.get_issues())

        return product_supermarket

    def product_for_price_update(self, _id):
        product_supermarket = self.__product_supermarket_repo.get_by_id(_id)
        if not product_supermarket.is_active_tracking:
            return None

        module_name = product_supermarket.supermarket.module_name
        class_name = product_supermarket.supermarket.class_name
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)

        product_supermarket.web_scraping = class_(HttpRequestsUtil())
        return product_supermarket

    def __new_product_supermarket(self, product, supermarket, price_update_url):
        return ProductSupermarket(product=product,
                                  supermarket=supermarket,
                                  price_update_url=price_update_url)

    def __get_product(self, product_id):
        product = self.__product_repo.get_by_id(product_id)
        if not product:
            raise ProductNotFoundException(product_id)
        return product

    def __get_supermarket(self, supermarket_id):
        supermarket = self.__supermarket_dao.get_by_id(supermarket_id)
        if not supermarket:
            raise SupermarketNotFoundException(supermarket_id)

        return supermarket
