from flask import Blueprint, request

from Services.productservice import ProductService

import json

app_product = Blueprint('app_product', __name__)


@app_product.route("/product", methods=['GET'])
def get_products():
    product_service = ProductService()
    products = product_service.get_products()
    return products













@app_product.route("/product/change_amount", methods=['PUT'])
def change_amount():
    request_data = request.get_json()
    productservice = ProductService()
    result = productservice.change_amount(request_data)
    if result:
        return json.dumps({
            "Result": result
        }), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({
            "Exception": 'Something is wrong',
        }), 200, {'ContentType': 'application/json'}
