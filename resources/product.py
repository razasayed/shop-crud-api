from flask import request
from flask_restful import Resource, reqparse
from models.product import ProductModel

class Product(Resource):
     parser = reqparse.RequestParser()
     parser.add_argument('name',
                        type=str,
                        required=True,
                        help="name cannot be blank!"
                        )
     parser.add_argument('description',
                        type=str,
                        required=True,
                        help="description cannot be blank!"
                        )
     parser.add_argument('logo_id',
                        type=int,
                        required=False
                        )

     def get(self):
        products = ProductModel.query.all()
        return {'Products':list(x.json() for x in products)}

     def post(self):
        data = Product.parser.parse_args()

        if ProductModel.find_by_name(data['name']):
            return {'message': "A product with name '{}' already exists.".format(data['name'])}, 400

        product = ProductModel(data['name'], data['description'])

        try:
            product.save_to_db()
        except:
            return {"message": "An error occurred inserting the product."}, 500

        return product.json(), 201

     def put(self,id):
        data = Product.parser.parse_args()
 
        product = ProductModel.query.filter_by(id=id).first()
 
        if product:
            product.name = data["name"]
            product.description = data["description"]
            if "logo_id" in data:
                product.logo_id = data["logo_id"]
        else:
            product = ProductModel(**data)
 
        product.save_to_db()
        return product.json()
