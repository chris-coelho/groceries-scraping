from src.domain.product_catalog.category import Category
from src.infra.data._repository_base import RepositoryBase


class CategoryRepository(RepositoryBase):
    def __init__(self):
        super().__init__(Category)

    def get_by_name(self, name):
        return super().session.query(Category).filter_by(name=name).one()
