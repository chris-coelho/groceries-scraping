from src.domain.entity_base import EntityBase


class ProductSupermarket(EntityBase):
    def __init__(self, product, supermarket, price_update_url, _id=None):
        self.id = super().get_id(_id)
        self.price_update_url = price_update_url
        self.is_active_tracking = False
        self.web_scraping = None
        self.current_price = 0
        self.last_update = None
        self.product = product
        self.product_id = product.id if product else None
        self.supermarket = supermarket
        self.supermarket_id = supermarket.id if supermarket else None
        self.pricing_history_list = []

    def __repr__(self):
        return "Entity (root): {}, ProductId: {}, SupermarketId: {}, IsActiveTracking: {}, Id: {}"\
            .format(self.__class__.__name__, self.product_id, self.supermarket_id, self.is_active_tracking, self.id)

    def as_json(self):
        formatted_last_update = self.last_update
        if self.last_update:
            formatted_last_update = self.last_update.strftime('%Y-%m-%d %H:%M:%S')
        return {
            'id': self.id,
            'price_update_url': self.price_update_url,
            'is_active_tracking': self.is_active_tracking,
            'current_price': self.current_price,
            'last_update': formatted_last_update,
            'product': {
                'id': self.product.id,
                'name': self.product.name
            },
            'supermarket': {
                'id': self.supermarket.id,
                'name': self.supermarket.name
            },
        }
