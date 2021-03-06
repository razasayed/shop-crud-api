from flask import Flask
from flask_restful import Resource, Api
from db import db
from resources import product, product_image, variant, variant_image

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:secret@db/shop-crud-api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(product.Product, '/product', '/product/<int:id>')
api.add_resource(product.ProductList, '/products')
api.add_resource(product_image.ProductImage, '/product/image')
api.add_resource(variant.Variant, '/variant', '/variant/<int:id>')
api.add_resource(variant.VariantList, '/variants')
api.add_resource(product.ProductVariantList, '/product/<int:product_id>/variants')
api.add_resource(variant_image.VariantImage, '/variant/image')
