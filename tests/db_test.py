from flask import Flask

from config import DbConfig
from src.domain.pricing_updates.supermarket_vo import SupermarketVO
from src.domain.product_catalog.category import Category
from src.domain.product_catalog.product import Product
from src.domain.product_catalog.sub_category import SubCategory
from src.infra.data._db import DbManager
from src.infra.data.category_repo import CategoryRepository
from src.infra.data.product_repo import ProductRepository
from src.infra.data.product_supermarket_repo import ProductSupermarketRepository
from src.infra.data.sub_category_repo import SubCategoryRepository
from src.infra.data.supermarket_dao import SupermarketDAO

app = Flask(__name__)
app.config.from_object(DbConfig('data.db'))

db = DbManager.start_db(app)

# db.create_all()


def make_load():
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

    print('inserting Milks...')
    milk_a = Product(name='Milk A', price=3.99, gtin='1234', sub_category=milks)
    milk_b = Product(name='Milk B', price=4.01, gtin='1235', sub_category=milks)
    prod_repo.save(milk_a)
    prod_repo.save(milk_b)
    prod_repo.commit()

    print('inserting Bread and Jelly from a list...')
    products = [
        Product(name='Bread', price=0.99, gtin='4321', sub_category=white_breads),
        Product(name='Jelly', price=5.99, gtin='1111', sub_category=low_calorie_jellies)
    ]
    prod_repo.save_many(products)
    prod_repo.commit()

def delete_load():
    print('deleting the Jelly..')
    prod_repo.delete(prod_repo.get_by_gtin('1111'))
    prod_repo.commit()

    print('after delete the Jelly:')
    for product in prod_repo.get_all():
        print(product)

    print('deleting the remaining products...')
    for product in prod_repo.get_all():
        prod_repo.delete(product)
    prod_repo.commit()

    print('Quantity of products after all deleting:', len(prod_repo.get_all()))


if __name__ == '__main__':
    category_repo = CategoryRepository()
    sub_category_repo = SubCategoryRepository()
    prod_repo = ProductRepository()
    product_supermarket_repo = ProductSupermarketRepository()

    # make_load()

    # print('consulting all Categories')
    # for category in category_repo.get_all():
    #     print(category)
    #
    # print('consulting all SubCategories')
    # for sub_category in sub_category_repo.get_all():
    #     print(sub_category)
    #
    # print('consulting all Products')
    # for product in prod_repo.get_all():
    #     print(product)
    #
    # print('consulting all products from Milks Subcategory...')
    # milks = sub_category_repo.get_by_name('Milks')
    # for product in milks.products:
    #     print(product)

    # supermarket_dao = SupermarketDAO()
    # supermarkets = [
    #     SupermarketVO(_id='d441a91ce8cc4d838eb3ccf69de3f932', name='Supermercados Boa', is_active=True),
    #     SupermarketVO(_id='cd12cdcdf7cb4296adc9752f45587534', name='Supermercado Test', is_active=False),
    #     SupermarketVO(_id='73dadb6c0d164e6b8a48c52a8aa1091f', name='Carrefour', is_active=True)
    # ]
    # supermarket_dao.save_many(supermarkets)

    # print('Supermarkets...')
    # for supermarket in SupermarketDAO().get_actives():
    #     print(supermarket)


    # product_supermarket_repo.delete(product_supermarket_repo.get_by_id('3d4064ff4a0e4520ba4b52d2a0063c53'))

    print('Supermarkets to tracking to the product "ASDA Soft White Toastie Thick Sliced Bread 800g"')
    for s in product_supermarket_repo.get_supermarkets_to_tracking_product('c99385eb17b148bba977a0959b725e13'):
        print(s.as_json())


    # delete_load()
