from src.domain.product_catalog.sub_category import SubCategory
from src.infra.data._repository_base import RepositoryBase


class SubCategoryRepository(RepositoryBase):
    def __init__(self):
        super().__init__(SubCategory)

    def get_by_name(self, name):
        return super().session.query(SubCategory).filter_by(name=name).one()
