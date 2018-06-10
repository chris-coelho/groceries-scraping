

class SupermarketVO:
    def __init__(self, _id, name, is_active, module_name=None, class_name=None):
        self.id = _id
        self.name = name
        self.is_active = is_active
        self.module_name = module_name
        self.class_name = class_name
        self.tracked_products = []

    def __repr__(self):
        return "ValueObject: {}, Name: {}, IsActive: {}, Id: {}"\
            .format(self.__class__.__name__, self.name, self.is_active, self.id)

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_active': self.is_active,
            'module_name': self.module_name,
            'class_name': self.class_name,
        }
