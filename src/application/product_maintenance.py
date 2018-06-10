from src.domain.product_catalog.product_factory import ProductFactory
from src.infra.data.category_repo import CategoryRepository
from src.infra.data.product_repo import ProductRepository
from src.infra.data.sub_category_repo import SubCategoryRepository


class ProductMaintenance:
    # This layer is responsible to accept the UI/APIs params and apply the Repos to get and persist data

    def __init__(self):
        self.__category_repo = CategoryRepository()
        self.__sub_category_repo = SubCategoryRepository()
        self.__product_repo = ProductRepository()
        self.__product_factory = ProductFactory(self.__category_repo,
                                                self.__sub_category_repo,
                                                self.__product_repo)

    def get_products_list(self):
        return self.__product_repo.get_all()

    def get_product(self, _id):
        return self.__product_repo.get_by_id(_id)

    def create_product(self, name, gtin, price, sub_category_id):
        new_product = self.__product_factory.default_product_with(name, gtin, price, sub_category_id)
        self.__product_repo.save(new_product)

    def update_product(self, _id, name, gtin, price, sub_category_id):
        product = self.__product_factory.default_product_to_update(_id, name, gtin, price, sub_category_id)
        self.__product_repo.save(product)
