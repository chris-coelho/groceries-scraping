from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import DbConfig
from src.apis.resources.product_resources import ProductsResource, CreateProductResource, ProductResource, \
    ProductSupermarketsToTrackResource, ProductActivateTrack, ProductDeactivateTrack
from src.domain.pricing_updates.supermarket_vo import SupermarketVO
from src.domain.product_catalog.category import Category
from src.domain.product_catalog.product import Product
from src.domain.product_catalog.sub_category import SubCategory
from src.infra.data._db import DbManager
from src.infra.data.category_repo import CategoryRepository
from src.infra.data.product_repo import ProductRepository
from src.infra.data.sub_category_repo import SubCategoryRepository
from src.infra.data.supermarket_dao import SupermarketDAO

app = Flask(__name__)
app.config.from_object(DbConfig)

api = Api(app)
api.add_resource(ProductsResource, '/apis/products')
api.add_resource(CreateProductResource, '/apis/product/create')
api.add_resource(ProductResource, '/apis/product/<string:id>')
api.add_resource(ProductSupermarketsToTrackResource, '/apis/product/<string:id>/supermarkets_track')
api.add_resource(ProductActivateTrack, '/apis/product/<string:id>/activate_track')
api.add_resource(ProductDeactivateTrack, '/apis/product/<string:id>/deactivate_track')

db = DbManager.start_db(app)
migrate = Migrate(app, db)


@app.before_first_request
def create_db():
    db.create_all()

    category_repo = CategoryRepository()
    sub_category_repo = SubCategoryRepository()
    prod_repo = ProductRepository()
    supermarket_dao = SupermarketDAO()

    # Categories
    if not category_repo.get_all():
        drinks = Category(name='Drinks')
        jellies = Category(name='Breads')
        breads = Category(name='Jellies')
        categories = [
            drinks,
            breads,
            jellies
        ]
        category_repo.save_many(categories)
        category_repo.commit()
    else:
        drinks = category_repo.get_by_name(name='Drinks')
        breads = category_repo.get_by_name(name='Breads')
        jellies = category_repo.get_by_name(name='Jellies')

    # SubCategories
    if not sub_category_repo.get_all():
        milks = SubCategory(name='Milks', category=drinks)
        low_calorie_jellies = SubCategory(name='Low Calories Jellies', category=jellies)
        white_breads = SubCategory(name='White Breads', category=breads)
        subcategories = [
            milks,
            low_calorie_jellies,
            white_breads
        ]
        sub_category_repo.save_many(subcategories)
        sub_category_repo.commit()
    else:
        milks = sub_category_repo.get_by_name(name='Milks')
        low_calorie_jellies = sub_category_repo.get_by_name(name='Low Calories Jellies')
        white_breads = sub_category_repo.get_by_name(name='White Breads')

    # Products
    if not prod_repo.get_all():
        products = [
            Product(name='Milk A', price=3.99, gtin='1234', sub_category=milks),
            Product(name='Milk B', price=4.01, gtin='1235', sub_category=milks),
            Product(name='Bread', price=0.99, gtin='4321', sub_category=white_breads),
            Product(name='Jelly', price=5.99, gtin='1111', sub_category=low_calorie_jellies)
        ]
        prod_repo.save_many(products)
        prod_repo.commit()

    # Supermarkets
    if not supermarket_dao.get_all():
        supermarkets = [
            SupermarketVO(_id='d441a91ce8cc4d838eb3ccf69de3f932',
                          name='Supermercados Boa',
                          is_active=True,
                          module_name='src.domain.pricing_updates.boa_scraping',
                          class_name='BoaScraping'),
            SupermarketVO(_id='73dadb6c0d164e6b8a48c52a8aa1091f',
                          name='Carrefour',
                          is_active=True,
                          module_name='src.domain.pricing_updates.carrefour_scraping',
                          class_name='CarrefourScraping')
        ]
        supermarket_dao.save_many(supermarkets)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

# supermarket_dao = SupermarketDAO()
# boa = supermarket_dao.get_by_id('d441a91ce8cc4d838eb3ccf69de3f932')
# boa.module_name = 'src.domain.pricing_updates.boa_scraping'
# boa.class_name = 'BoaScraping'
#
# carrefour = supermarket_dao.get_by_id('73dadb6c0d164e6b8a48c52a8aa1091f')
# carrefour.module_name = 'src.domain.pricing_updates.carrefour_scraping'
# carrefour.class_name = 'CarrefourScraping'
#
# supermarket_dao.save_many([boa, carrefour])
