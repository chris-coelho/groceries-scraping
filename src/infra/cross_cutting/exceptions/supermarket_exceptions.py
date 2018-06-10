from src.infra.cross_cutting.exceptions._exception_base import ExceptionBase


class SupermarketException(ExceptionBase):
    def __init__(self, messages):
        super().__init__(messages)


class SupermarketNotFoundException(SupermarketException):
    def __init__(self, _id):
        if _id:
            message = 'Supermarket {} not found!'.format(_id)
        else:
            message = 'Supermarket not found!'
        super().__init__(message)
