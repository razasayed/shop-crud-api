from db import db

class VariantImageModel(db.Model):
    __tablename__ = 'variant_images'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100))
    variant_id = db.Column(db.Integer, db.ForeignKey('variants.id'))
    variant = db.relationship('VariantModel')

    def __init__(self, url, variant_id):
        self.url = url
        self.variant_id = variant_id

    def json(self):
        return {'url': self.url}

    @classmethod
    def find_by_url(cls, url):
        return cls.query.filter_by(url=url).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
