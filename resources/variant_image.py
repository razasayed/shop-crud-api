from flask import request
from flask_restful import Resource, reqparse
from models.variant_image import VariantImageModel

class VariantImage(Resource):
     parser = reqparse.RequestParser()
     parser.add_argument('url',
                        type=str,
                        required=True,
                        help="variant image url cannot be blank!"
                        )
     parser.add_argument('variant_id',
                        type=int,
                        required=True,
                        help="variant_id is required"
                        )

     def post(self):
        data = VariantImage.parser.parse_args()

        if VariantImageModel.find_by_url(data['url']):
            return {'message': "An image with url '{}' already exists.".format(data['url'])}, 400

        variant_image = VariantImageModel(**data)

        try:
            variant_image.save_to_db()
        except:
            return {"message": "An error occurred inserting the image."}, 500

        return variant_image.json(), 201
