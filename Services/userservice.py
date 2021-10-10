from sqlalchemy import update

from Models.usermodel import User
from __main__ import db

class UserService:
    def create_user(self, request_data):
        user = User()
        user.username = request_data['username']
        user.email = request_data['email']
        user.password = request_data['password']
        db.session.add(user)
        db.session.commit()

    def login(self, request_data):
        user = db.session.query(User).filter(User.email == request_data['email']).first()
        if user and user.password == request_data['password']:
            return user

        return False






    def change_password(self, request_data):
        user = db.session.query(User).filter(User.id == request_data['id']).first()
        if user and user.password != request_data['new_password']:
            db.session.execute(update(User).where(User.id == request_data['id']).values(password=request_data['new_password']))
            db.session.commit()
            return True
        return False


