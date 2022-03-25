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

     def post(self):
        data = request.get_json()
        print('Data is {}', data)

        if ProductModel.find_by_name(data['name']):
            return {'message': "A product with name '{}' already exists.".format(data['name'])}, 400

        product = ProductModel(data['name'], data['description'])

        try:
            product.save_to_db()
        except:
            return {"message": "An error occurred inserting the product."}, 500

        return product.json(), 201
