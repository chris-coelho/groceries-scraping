from src.domain.pricing_updates.product_supermarket_factory import ProductSupermarketFactory
from src.infra.data.product_repo import ProductRepository
from src.infra.data.product_supermarket_repo import ProductSupermarketRepository
from src.infra.data.supermarket_dao import SupermarketDAO


class PricingUpdate:
    def __init__(self, product_repo=None, supermarket_dao=None, product_supermarket_repo=None):
        self.__product_repo = product_repo if product_repo else ProductRepository()
        self.__supermarket_dao = supermarket_dao if supermarket_dao else SupermarketDAO()
        self.__product_supermarket_repo = product_supermarket_repo if product_supermarket_repo else \
            ProductSupermarketRepository()
        self.__product_supermarket_factory = ProductSupermarketFactory(self.__product_repo,
                                                                       self.__supermarket_dao,
                                                                       self.__product_supermarket_repo)

    def get_supermarkets_to_tracking(self, product_id):
        return self.__product_supermarket_repo.get_supermarkets_to_tracking_product(product_id)

    def activate_track(self, product_id, supermarket_id, price_update_url):
        product_to_tracking = self.__product_supermarket_factory.activate_tracking(product_id,
                                                                                   supermarket_id,
                                                                                   price_update_url)
        self.__product_supermarket_repo.save(product_to_tracking)

    def deactivate_track(self, product_id, supermarket_id):
        product_to_tracking = self.__product_supermarket_factory.deactivate_tracking(product_id, supermarket_id)
        self.__product_supermarket_repo.save(product_to_tracking)
