from Models.product import Product

from sqlalchemy import update

from __main__ import db
import json


class ProductService:
    def get_products(self):
        products = db.session.query(Product).all()
        if products:
            serialized_products = []
            for product in products:
                serialized_products.append({
                    "id": product.id,
                    "name": product.name,
                    "description": product.description,
                    "amount": product.amount,
                    "image_url": product.image_url,
                    "price": product.price
                })
            return json.dumps(serialized_products)

        return False

    def change_amount(self, request_data):
        product = db.session.query(Product).filter(Product.id == request_data['id']).first()
        if product and request_data['new_amount']:
            new_amount = product.amount - request_data['new_amount']
            db.session.execute(update(Product).where(Product.id == request_data['id']).values(amount=new_amount))
            db.session.commit()
            return new_amount
        return False
