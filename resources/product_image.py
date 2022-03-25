from flask import request
from flask_restful import Resource, reqparse
from models.product_image import ProductImageModel

class ProductImage(Resource):
     parser = reqparse.RequestParser()
     parser.add_argument('url',
                        type=str,
                        required=True,
                        help="product image url cannot be blank!"
                        )

     def post(self):
        data = request.get_json()

        if ProductImageModel.find_by_url(data['url']):
            return {'message': "An image with url '{}' already exists.".format(data['url'])}, 400

        product_image = ProductImageModel(data['url'])

        try:
            product_image.save_to_db()
        except:
            return {"message": "An error occurred inserting the image."}, 500

        return product_image.json(), 201
