from datetime import datetime

from flask import Flask

from config import DbConfig
from src.domain.pricing_updates.boa_scraping import BoaScraping
from src.domain.pricing_updates.carrefour_scraping import CarrefourScraping
from src.domain.pricing_updates.product_supermarket_factory import ProductSupermarketFactory
from src.infra.data._db import DbManager
from src.infra.data.product_repo import ProductRepository
from src.infra.data.product_supermarket_repo import ProductSupermarketRepository
from src.infra.data.supermarket_dao import SupermarketDAO


def get_preco(url, webscraping):
    return webscraping.get_price(url)

app = Flask(__name__)
app.config.from_object(DbConfig('data.db'))

db = DbManager.start_db(app)


if __name__ == '__main__':
    # boa_scraping = BoaScraping()
    # carrefour_scraping = CarrefourScraping()
    #
    # margarina_boa = 'https://www.supermercadosboa.com.br/produto.php?_p=181167'
    # margarina_carrefour = 'https://www.carrefour.com.br/Margarina-Cremosa-com-Sal-Qualy-500g/p/149730'
    # print('Margarina Boa - Preço: {}'.format(get_preco(margarina_boa, boa_scraping)))
    # print('Margarina Carrefour - Preço: {}'.format(get_preco(margarina_carrefour, carrefour_scraping)))
    #
    # chantilly_boa = 'https://www.supermercadosboa.com.br/produto.php?_p=181747'
    # chantilly_carrefour = 'https://www.carrefour.com.br/Creme-Vegetal-Tipo-Chantilly-Tradicional-Vigor-250g/p/140201'
    # print('Chantilly Boa - Preço: {}'.format(get_preco(chantilly_boa, boa_scraping)))
    # print('Chantilly Carrefour - Preço: {}'.format(get_preco(chantilly_carrefour, carrefour_scraping)))

    product_repo = ProductRepository()
    supermarket_dao = SupermarketDAO()
    product_supermarket_repo = ProductSupermarketRepository()

    for ps in product_supermarket_repo.get_supermarkets_allowed_to_price_update():
        product_supermarket = ProductSupermarketFactory(product_repo, supermarket_dao, product_supermarket_repo)\
            .product_for_price_update(_id=ps.id)

        price = product_supermarket.web_scraping.get_price(product_supermarket.price_update_url)
        product_supermarket.current_price = price
        product_supermarket.last_update = datetime.now()

        product_supermarket_repo.save(product_supermarket)

        print('product: {}, supermarket: {}, price: {}, updated on: {}'.format(product_supermarket.product.name,
                                                                               product_supermarket.supermarket.name,
                                                                               product_supermarket.current_price,
                                                                               product_supermarket.last_update))
