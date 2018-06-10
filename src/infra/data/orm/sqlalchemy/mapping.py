from sqlalchemy import Table, MetaData, Column, String, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import mapper, relationship

from src.domain.pricing_updates.pricing_history import PricingHistory
from src.domain.pricing_updates.product_supermarket import ProductSupermarket
from src.domain.pricing_updates.supermarket_vo import SupermarketVO
from src.domain.product_catalog.category import Category
from src.domain.product_catalog.product import Product
from src.domain.product_catalog.sub_category import SubCategory

custom_metadata = MetaData()

category = Table('category', custom_metadata,
                 Column('id', String(32), primary_key=True),
                 Column('name', String(50), nullable=False))

sub_category = Table('sub_category', custom_metadata,
                     Column('id', String(32), primary_key=True),
                     Column('name', String(50), nullable=False),
                     Column('category_id', String(32), ForeignKey('category.id')))

product = Table('product', custom_metadata,
                Column('id', String(32), primary_key=True),
                Column('name', String(100), nullable=False),
                Column('gtin', String(25), unique=True),
                Column('price', Float(precision=2)),
                Column('sub_category_id', String(32), ForeignKey('sub_category.id')))

supermarket_dao = Table('supermarket_dao', custom_metadata,
                        Column('id', String(32), primary_key=True),
                        Column('name', String(50), nullable=False),
                        Column('is_active', Boolean, nullable=False),
                        Column('module_name', String(128)),
                        Column('class_name', String(50)))

product_supermarket = Table('product_supermarket', custom_metadata,
                            Column('id', String(32), primary_key=True),
                            Column('product_id', String(32), ForeignKey('product.id')),
                            Column('supermarket_id', String(32), ForeignKey('supermarket_dao.id')),
                            Column('is_active_tracking', Boolean, nullable=False),
                            Column('price_update_url', String(500)),
                            Column('current_price', Float),
                            Column('last_update', DateTime))

pricing_history = Table('pricing_history', custom_metadata,
                        Column('id', String(32), primary_key=True),
                        Column('product_supermarket_id', String(32), ForeignKey('product_supermarket.id')),
                        Column('price', Float, nullable=False),
                        Column('update_on', DateTime, nullable=False))


mapper(Category, category, properties={
    'subcategories': relationship(SubCategory, backref='category', order_by=sub_category.c.id)
})
mapper(SubCategory, sub_category, properties={
    'products': relationship(Product, backref='sub_category', order_by=product.c.id)
})
mapper(Product, product, properties={
    'tracked_supermarkets': relationship(ProductSupermarket, backref='product', order_by=product_supermarket.c.id)
})
mapper(SupermarketVO, supermarket_dao, properties={
    'tracked_products': relationship(ProductSupermarket, backref='supermarket', order_by=product_supermarket.c.id)
})
mapper(ProductSupermarket, product_supermarket, properties={
    'pricing_history_list': relationship(PricingHistory, backref='product_supermarket', order_by=pricing_history.c.id)
})
mapper(PricingHistory, pricing_history)
