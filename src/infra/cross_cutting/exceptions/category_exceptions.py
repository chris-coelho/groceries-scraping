from src.infra.cross_cutting.exceptions._exception_base import ExceptionBase


class CategoryException(ExceptionBase):
    def __init__(self, messages):
        super().__init__(messages)


class CategoryNotFoundException(CategoryException):
    def __init__(self, _id):
        if _id:
            message = 'Category {} not found!'.format(_id)
        else:
            message = 'Category not found!'
        super().__init__(message)
