from db import db

class VariantModel(db.Model):
    __tablename__ = 'variants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    size = db.Column(db.String(10))
    color = db.Column(db.String(50))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship('ProductModel')
    created_at  = db.Column(db.DateTime, server_default=db.func.now())
    updated_at  = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name, size, color, product_id):
        self.name = name
        self.size = size
        self.color = color
        self.product_id = product_id

    def json(self):
        return {'name': self.name, 'size': self.size, 'color': self.color, 'product_id': self.product_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
