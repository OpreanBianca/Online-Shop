from __main__ import db
from sqlalchemy import ForeignKey


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    product_id = db.Column(db.Integer, ForeignKey('product.id'))







