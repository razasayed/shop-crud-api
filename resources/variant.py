from flask import request
from flask_restful import Resource, reqparse
from models.variant import VariantModel
from models.product import ProductModel

class Variant(Resource):
     parser = reqparse.RequestParser()
     parser.add_argument('name',
                        type=str,
                        required=True,
                        help="name cannot be blank!"
                        )
     parser.add_argument('size',
                        type=str,
                        required=True,
                        help="size is required"
                        )
     parser.add_argument('color',
                        type=str,
                        required=True,
                        help="color is required"
                        )
     parser.add_argument('product_id',
                        type=int,
                        required=True,
                        help="product_id is required"
                        )
                        
     def get(self, id):
        variant = VariantModel.query.get(id)
        if variant:
            return variant.json()
        return {'message': 'Variant not found'}, 404

     def post(self):
        data = Variant.parser.parse_args()

        if VariantModel.find_by_name(data['name']):
            return {'message': "A variant with name '{}' already exists.".format(data['name'])}, 400

        variant = VariantModel(**data)

        try:
            variant.save_to_db()
        except:
            return {"message": "An error occurred inserting the variant."}, 500

        return variant.json(), 201

     def put(self,id):
        data = Variant.parser.parse_args()
 
        variant = VariantModel.query.filter_by(id=id).first()
 
        if variant:
            variant.name = data["name"]
            variant.size = data["size"]
            variant.color = data["color"]
            variant.product_id = data["product_id"]
        else:
            variant = VariantModel(**data)
 
        variant.save_to_db()
        return variant.json()

class VariantList(Resource):
    def get(self):
        return {'variants': list(map(lambda x: x.json(), VariantModel.query.all()))}
