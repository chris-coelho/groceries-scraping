from src.infra.cross_cutting.exceptions._exception_base import ExceptionBase


class ProductSupermarketException(ExceptionBase):
        def __init__(self, messages):
            super().__init__(messages)
