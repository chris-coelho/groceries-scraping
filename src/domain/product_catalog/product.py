from src.domain.entity_base import EntityBase


class Product(EntityBase):
    def __init__(self, name, gtin, price, sub_category, _id=None):
        self.id = super().get_id(_id)
        self.name = name
        self.gtin = gtin
        self.price = price
        self.sub_category = sub_category
        self.sub_category_id = sub_category.id if sub_category else None
        self.tracked_supermarkets = []

    def __repr__(self):
        return "Entity (root): {}, Name: {}, GTIN: {}, Price: {}, SubCategoryID: {}, Id: {}"\
            .format(self.__class__.__name__, self.name, self.gtin, self.price, self.sub_category_id, self.id)

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'gtin': self.gtin,
            'price': self.price,
            'sub_category': {
                'id': self.sub_category_id,
                'name': self.sub_category.name,
            },
        }
