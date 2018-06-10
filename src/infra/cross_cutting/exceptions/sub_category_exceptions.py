from src.infra.cross_cutting.exceptions._exception_base import ExceptionBase


class SubCategoryException(ExceptionBase):
    def __init__(self, messages):
        super().__init__(messages)


class SubCategoryNotFoundException(SubCategoryException):
    def __init__(self, _id):
        if _id:
            message = 'Subcategory {} not found!'.format(_id)
        else:
            message = 'Subcategory not found!'
        super().__init__(message)


class SubCategoryAlreadyExistsException(SubCategoryException):
    def __init__(self, entity):
        super().__init__("Subcategory already exists: {}".format(entity))


class CategoryRequiredException(SubCategoryException):
    def __init__(self, _id):
        if _id:
            message = 'Category {} not found!'.format(_id)
        else:
            message = 'Category required!'
        super().__init__(message)
