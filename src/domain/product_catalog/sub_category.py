from src.domain.entity_base import EntityBase


class SubCategory(EntityBase):
    def __init__(self, name, category, _id=None):
        self.id = super().get_id(_id)
        self.name = name
        self.category = category
        self.category_id = category.id if category else None
        self.products = []

    def __repr__(self):
        return "Entity: {}, Name: {}, CategoryID: {}, Id: {}"\
            .format(self.__class__.__name__, self.name, self.category_id, self.id)

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': {
                'id': self.category.id,
                'name': self.category.name
            },
            'products': [],
        }
