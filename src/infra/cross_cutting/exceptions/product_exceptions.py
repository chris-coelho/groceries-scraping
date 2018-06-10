from src.infra.cross_cutting.exceptions._exception_base import ExceptionBase


class ProductException(ExceptionBase):
    def __init__(self, messages):
        super().__init__(messages)


class ProductNotFoundException(ProductException):
    def __init__(self, _id):
        if _id:
            message = 'Product {} not found!'.format(_id)
        else:
            message = 'Product not found!'
        super().__init__(message)


class ProductAlreadyExistsException(ProductException):
    def __init__(self, entity):
        super().__init__("Product already exists: {}".format(entity))


class ProductWithDuplicatedGtinException(ProductException):
    def __init__(self, gtin):
        super().__init__("Already exists another product with the same GTIN {}.".format(gtin))


class ProductRequiresSubCategoryException(ProductException):
    def __init__(self, _id):
        if _id:
            message = 'Subcategory {} not found!'.format(_id)
        else:
            message = 'Subcategory required!'
        super().__init__(message)
