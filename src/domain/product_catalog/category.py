from src.domain.entity_base import EntityBase


class Category(EntityBase):
    def __init__(self, name, _id=None):
        self.id = super().get_id(_id)
        self.name = name
        self.subcategories = []

    def __repr__(self):
        return "Entity: {}, Name: {}, Id: {}"\
            .format(self.__class__.__name__, self.name, self.id)

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'subcategories': [],
        }