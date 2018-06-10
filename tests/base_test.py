from unittest import TestCase

from flask import Flask

from config import DbConfig
from src.domain.product_catalog.category import Category
from src.domain.product_catalog.sub_category import SubCategory
from src.infra.data._db import DbManager
from src.infra.data.category_repo import CategoryRepository
from src.infra.data.product_repo import ProductRepository
from src.infra.data.product_supermarket_repo import ProductSupermarketRepository
from src.infra.data.sub_category_repo import SubCategoryRepository
from src.infra.data.supermarket_dao import SupermarketDAO

app = Flask(__name__)
app.config.from_object(DbConfig('test.db'))
db = DbManager.start_db(app)


class BaseTest(TestCase):
    def setUp(self):
        with app.app_context():
            db.create_all()

        self.category_repo = CategoryRepository()
        self.sub_category_repo = SubCategoryRepository()
        self.product_repo = ProductRepository()
        self.supermarket_dao = SupermarketDAO()
        self.product_supermarket_repo = ProductSupermarketRepository()

        self.category = Category(_id='bd932a425cf040509a6071ea9b4bc138',
                                 name='Breads')
        self.sub_category = SubCategory(_id='5bcd3cca9a3e4065a248c821cd2f1f32',
                                        name='Gluten Free Breads',
                                        category=self.category)

        self.category_repo.save(self.category)
        self.sub_category_repo.save(self.sub_category)

        self.app_context = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
