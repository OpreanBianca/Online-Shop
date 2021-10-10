import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists
from flask_cors import CORS, cross_origin

db = SQLAlchemy()

from Models.usermodel import User
from Models.product import Product
from Models.cart import Cart


def create_app(debug=True):
    app = Flask(__name__)
    CORS(app)
    cors = CORS(app, resource={
        r"/*": {
            "origins": "*"
        }
    })
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.debug = debug

    file_path = os.path.abspath(os.getcwd()) + "\database.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from Controllers.health import app_health
    from Controllers.usercontroller import app_user
    from Controllers.productcontroller import app_product
    app.register_blueprint(app_health)
    app.register_blueprint(app_user)
    app.register_blueprint(app_product)

    return app


app = create_app(True)

with app.app_context():
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        db.create_all()
        admin = User(username='Admin', email='a@a.ro', password='admin')
        db.session.add(admin)
        product1 = Product(name=' Samsung Galaxy S20 FE (2021)',
                       description='The 4500 mAh battery (typical) gives your phone the power it needs to last a full day and is smart enough to save power for when you really need it. With the built-in 128 GB and the ability to store up to 1 TB on a microSD card, the only limit to what you can store is just what you can create and download yourself. Classified at IP68 in terms of water and dust resistance, this phone withstands a depth of 1.5 meters underwater for up to 30 minutes. So you can play or film even if the phone gets a little wet.',
                       amount='32', price='2.339 $',
                       image_url=r'C:\Users\oprea\Desktop\Proiect PA\Assets\Images\Telefon mobil Samsung Galaxy S20 FE (2021).webp')
        db.session.add(product1)
        product2 = Product(name=' Samsung Galaxy A21s',
                       description='When youre away from home, you need a phone whose battery lasts. A 5,000mAh battery (typical) * gives you the power to transmit, share and play. And if you run out of power, connect and power up to 15W of fast charging. The Alxy A21s has fast processing and generous storage space, so you can focus now. An advanced Octa-core processor and 3 GB of RAM offer smooth and efficient performance. Download more and delete less with 32 GB of internal storage. Add even more with a 512 GB microSD card.',
                       amount='10', price='599 $',
                       image_url=r'C:\Users\oprea\Desktop\Proiect PA\Assets\Images\Telefon mobil Samsung Galaxy A21s.webp')
        db.session.add(product2)
        product3 = Product(name='Samsung Galaxy Buds Plus Bluetooth Headset',
                       description='A complex, natural sound, offered by the new Galaxy Buds + product, with a dynamic two-way speaker system and optimized driver. The strong bass and the clearly played high notes will make you move to the rhythm of the music, wherever you are.',
                       amount='23', price='475 $',
                       image_url=r'C:\Users\oprea\Desktop\Proiect PA\Assets\Images\Casti bluetooth Samsung Galaxy Buds Plus.webp')
        db.session.add(product3)
        product4 = Product(name='Laptop Allview Allbook H',
                       description='Allbook H comes equipped with Intel Celeron N4000, a model that belongs to the new generation of processors, which promises superior reaction speeds, 20% higher graphics processing, dual cache and low power consumption compared to the previous generation. It is backed by a 4GB RAM to ensure a successful experience every time.',
                       amount='42', price='1.299 $',
                       image_url=r'C:\Users\oprea\Desktop\Proiect PA\Assets\Images\Laptop Allview Allbook H.webp')
        db.session.add(product4)
        product5 = Product(name='Laptop Apple MacBook Air 13-inch',
                       description='The image signal processor in the M1 chip helps you look your best for every FaceTime call and video conference. Three built-in microphones ensure that what you say is heard whether you are on call, dictating a note or asking Siri about the weather. GPU speed up to 5 times faster. The most advanced neural motor for machine learning up to 9 times faster.',
                       amount='17', price='4.999 $',
                       image_url=r'C:\Users\oprea\Desktop\Proiect PA\Assets\Images\Laptop Apple MacBook Air 13-inch.webp')
        db.session.add(product5)
        product6 = Product(name='Canon EOS 800D DSLR camera',
                       description='A state-of-the-art 24.2 megapixel sensor and APS-C size capture amazing details, even in difficult conditions. Take photos and movies below or above your head, using the EOS 800D s variable angle touch screen to compose the scene.',
                       amount='50', price='2.799 $',
                       image_url=r'C:\Users\oprea\Desktop\Proiect PA\Assets\Images\Aparat foto DSLR Canon EOS 800D.webp')
        db.session.add(product6)
        cart1 = Cart(user_id='1', product_id='5')
        db.session.add(cart1)

        db.session.commit()




if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
