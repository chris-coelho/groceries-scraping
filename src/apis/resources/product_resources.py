from flask_restful import Resource, reqparse

from src.application.pricing_update import PricingUpdate
from src.application.product_maintenance import ProductMaintenance
from src.infra.cross_cutting.exceptions._handle_exception_messages import handle_message
from src.infra.cross_cutting.exceptions.product_exceptions import ProductException


class ProductsResource(Resource):
    def __init__(self):
        self.__product_maintenance = ProductMaintenance()

    def get(self):
        return {'products': [product.as_json() for product in self.__product_maintenance.get_products_list()]}


class CreateProductResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='Invalid field')
    parser.add_argument('gtin',
                        type=str,
                        required=True,
                        help='Invalid field')
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='Invalid field')
    parser.add_argument('sub_category_id',
                        type=str,
                        required=True,
                        help='Invalid field')

    def __init__(self):
        self.__product_maintenance = ProductMaintenance()

    def post(self):
        data = CreateProductResource.parser.parse_args()

        try:
            self.__product_maintenance.create_product(name=data['name'],
                                                      gtin=data['gtin'],
                                                      price=data['price'],
                                                      sub_category_id=data['sub_category_id'])
            return {'message': 'product successfully created'}, 201
        except ProductException as e:
            return {'message': handle_message(e)}, 409
        except Exception as e:
            return {'message': handle_message(e)}, 500


class ProductResource(Resource):
    def __init__(self):
        self.__product_maintenance = ProductMaintenance()

    def get(self, id):

        try:
            product = self.__product_maintenance.get_product(id)
            if not product:
                return {'message': 'Product {} not found.'.format(id)}, 409

            return product.as_json() # avaliar o impacto de alterações no objeto product afetar os clientes da API
        except ProductException as e:
            return {'message': handle_message(e)}, 409
        except Exception as e:
            return {'message': handle_message(e)}, 500

    def put(self, id):
        data = CreateProductResource.parser.parse_args()

        try:
            self.__product_maintenance.update_product(str(id),
                                                      data['name'],
                                                      data['gtin'],
                                                      data['price'],
                                                      data['sub_category_id'])

            return {'message': 'product successfully updated.'}, 201
        except ProductException as e:
            return {'message': handle_message(e)}, 409
        except Exception as e:
            return {'message': handle_message(e)}, 500


class ProductSupermarketsToTrackResource(Resource):
    def __init__(self):
        self.__pricing_update = PricingUpdate()

    def get(self, id):
        try:
            product_supermarkets = self.__pricing_update.get_supermarkets_to_tracking(id)
            return {'supermarkets_to_track': [ps.as_json() for ps in product_supermarkets]}
        except ProductException as e:
            return {'message': handle_message(e)}, 409
        except Exception as e:
            return {'message': handle_message(e)}, 500


class ProductActivateTrack(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('supermarket_id',
                        type=str,
                        required=True,
                        help='Invalid field')
    parser.add_argument('price_update_url',
                        type=str,
                        required=True,
                        help='Invalid field')

    def __init__(self):
        self.__pricing_update = PricingUpdate()

    def put(self, id):
        data = ProductActivateTrack.parser.parse_args()

        try:
            self.__pricing_update.activate_track(product_id=str(id),
                                                 supermarket_id=data['supermarket_id'],
                                                 price_update_url=data['price_update_url'])

            return {'message': 'product successfully marked to tracking.'}, 201
        except ProductException as e:
            return {'message': handle_message(e)}, 409
        except Exception as e:
            return {'message': handle_message(e)}, 500


class ProductDeactivateTrack(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('supermarket_id',
                        type=str,
                        required=True,
                        help='Invalid field')

    def __init__(self):
        self.__pricing_update = PricingUpdate()

    def put(self, id):
        data = ProductDeactivateTrack.parser.parse_args()

        try:
            self.__pricing_update.deactivate_track(product_id=str(id), supermarket_id=data['supermarket_id'])

            return {'message': 'product successfully unmarked to tracking.'}, 201
        except ProductException as e:
            return {'message': handle_message(e)}, 409
        except Exception as e:
            return {'message': handle_message(e)}, 500
