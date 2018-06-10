from src.domain.product_catalog.product import Product
from src.infra.data._repository_base import RepositoryBase


class ProductRepository(RepositoryBase):
    def __init__(self):
        super().__init__(Product)

    def get_by_name(self, name):
        return super().session.query(Product).filter(name.like(name.join('%'))).all()

    def get_by_gtin(self, gtin):
        return super().session.query(Product).filter_by(gtin=gtin).one_or_none()

    def gtin_duplicated(self, gtin):
        return super().session.query(Product).filter_by(gtin=gtin).count() > 1
