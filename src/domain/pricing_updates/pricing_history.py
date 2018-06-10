from src.domain.entity_base import EntityBase


class PricingHistory(EntityBase):
    def __init__(self, product_supermarket_id, price, update_on, _id=None):
        self.id = super().get_id(_id)
        self.product_supermarket_id = product_supermarket_id
        self.price = price
        self.update_on = update_on

    def __repr__(self):
        return "Entity: {}, ProductSupermarketId: {}, Price: {}, UpdateOn: {}, Id: {}"\
            .format(self.__class__.__name__, self.product_supermarket_id, self.price, self.update_on, self.id)

    def as_json(self):
        return {
            'id': self.id,
            'product_supermarket_id': self.product_supermarket_id,
            'price': self.price,
            'update_on': self.update_on.strftime('%Y-%m-%d %H:%M:%S')
        }