from db import db

class ProductImageModel(db.Model):
    __tablename__ = 'product_images'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship('ProductModel',foreign_keys=[product_id])

    def __init__(self, id, url, product_id):
        self.url = url
        self.product_id = product_id

    def json(self):
        return {'url': self.url}

    @classmethod
    def find_by_url(cls, name):
        return cls.query.filter_by(url=url).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
