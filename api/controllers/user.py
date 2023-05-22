# app/controllers/user_controller.py

from passlib.hash import bcrypt

from api.models import UserModel
from api.schemas import UserSchema
from api.utils.database import db
from api.utils.auth import authenticate, generate_token
from api.config import Config
user_schema = UserSchema()

def create_user(data):
    username = data['username']
    password = data['password']
    
    hashed_password = bcrypt.hash(password)
    starting_balance = Config.USER_STARTING_BALANCE

    new_user = UserModel(username=username, password=hashed_password, status='active')
    db.session.add(new_user)
    db.session.commit()

    return user_schema.dump(new_user)

def get_user(user_id):
    user = UserModel.query.get(user_id)
    if user:
        return user_schema.dump(user)
    return None


def login(data):
    username = data['username']
    password = data['password']

    user = authenticate(username, password)
    if user:
        access_token = generate_token(user)
        return {'access_token': access_token}, 200

    return {'message': 'Invalid credentials'}, 401  