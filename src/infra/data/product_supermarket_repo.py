from src.domain.pricing_updates.product_supermarket import ProductSupermarket
from src.infra.cross_cutting.exceptions.product_exceptions import ProductNotFoundException
from src.infra.data._repository_base import RepositoryBase
from src.infra.data.product_repo import ProductRepository
from src.infra.data.supermarket_dao import SupermarketDAO


class ProductSupermarketRepository(RepositoryBase):
    def __init__(self):
        super().__init__(ProductSupermarket)

    def get_unique(self, product_id, supermarket_id):
        return super().session.query(ProductSupermarket)\
            .filter_by(supermarket_id=supermarket_id)\
            .filter_by(product_id=product_id).one_or_none()

    def get_supermarkets_to_tracking_product(self, product_id):
        product = ProductRepository().get_by_id(product_id)
        if not product:
            raise ProductNotFoundException(product_id)

        active_supermarkets = SupermarketDAO().get_actives()
        product_supermarkets = super().session.query(ProductSupermarket).filter_by(product_id=product_id).all()

        supermarkets_to_track = []
        for active_supermarket in active_supermarkets:
            found = False
            for product_supermarket in product_supermarkets:
                if product_supermarket.supermarket == active_supermarket:
                    supermarkets_to_track.append(product_supermarket)
                    found = True
            if not found:
                supermarkets_to_track.append(ProductSupermarket(
                    product=product,
                    supermarket=active_supermarket,
                    price_update_url=None
                ))

        return supermarkets_to_track

    def get_supermarkets_allowed_to_price_update(self):
        return super().session.query(ProductSupermarket).filter_by(is_active_tracking=True).all()
