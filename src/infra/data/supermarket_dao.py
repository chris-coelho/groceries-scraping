from src.domain.pricing_updates.supermarket_vo import SupermarketVO
from src.infra.data._dao_base import DaoBase


class SupermarketDAO(DaoBase):
    def __init__(self):
        super().__init__(SupermarketVO)

    def get_actives(self):
        return super().session.query(SupermarketVO).filter_by(is_active=True).all()
