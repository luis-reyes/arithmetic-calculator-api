# app/v1/resources/user_resource.py

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import SQLAlchemyError,IntegrityError

from api.controllers.user import create_user, get_user
from api.schemas import UserSchema
from api.controllers.user import login



user_blp = Blueprint('user', __name__)

@user_blp.route('/register')
class User(MethodView):
    @user_blp.arguments(UserSchema)
    @user_blp.response(201, UserSchema)
    def post(self, data):
        
        try:
            created_user = create_user(data)
        except IntegrityError:
            abort(
                400,
                message="User with this email already exists."
            )
        except SQLAlchemyError:
            abort(500, message="An error ocurred while saving registering the user.")

        return created_user, 201

@user_blp.route('/<int:user_id>')
class SpecificUser(MethodView):
    @jwt_required()
    def get(self, user_id):
        current_user_id = get_jwt_identity()
        if current_user_id != user_id:
            abort(403, message='User is not Authorized to view the requested information.')

        user = get_user(user_id)
        if not user:
            abort(404, message='User not found')

        return user

@user_blp.route('/login', endpoint='login')
class UserLogin(MethodView):
    @user_blp.arguments(UserSchema)
    def post(self, data):
        response, status_code = login(data)
        if status_code == 200:
            return response

        abort(status_code, message=response['message'])