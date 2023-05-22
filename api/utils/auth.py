from flask_jwt_extended import create_access_token
from passlib.hash import bcrypt

from api.models import UserModel

def verify_password(plain_password, hashed_password):
    return bcrypt.verify(plain_password, hashed_password)

def authenticate(username, password):
    user = UserModel.query.filter_by(username=username).first()
    if user and verify_password(password, user.password):
        return user

def generate_token(user):
    access_token = create_access_token(identity=user.id)
    return access_token
