from flask.views import MethodView
from flask import request
from flask_smorest import Blueprint
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.controllers.record import calculate_operation,get_all_transactions, delete_transaction
from api.controllers.user import get_user

transaction_blp = Blueprint('transaction', __name__)

@transaction_blp.route('/',strict_slashes=False)
class Transaction(MethodView):
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def get(self):

        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)

        current_user_id = get_jwt_identity()
        operation_id = request.args.get('operation_id')


        result, error = get_all_transactions(
            page = page,
            per_page = per_page,
            operation_id=operation_id,
            user_id=current_user_id,
        )
        
        if error:
            return {'message': error}, 400

        return result, 200


    @jwt_required()
    @cross_origin(supports_credentials=True)
    def post(self):
        data = request.get_json()

        if not data:
            return {'message': 'No input data provided'}, 400

        current_user_id = get_jwt_identity()
        user = get_user(current_user_id)
        if not user:
            return {'message': 'User not found'}, 404
        
        operation_id = data.get('operation_id')
        num1 = data.get('num_1')
        num2 = data.get('num_2')
        if not num1:
            num1 = 0
        if not num2:
            num2 = 0
        if not operation_id :
            return {'message': 'Missing required fields'}, 400

        result, error = calculate_operation(
            user_id=current_user_id,
            operation_id=operation_id,
            num1=num1,
            num2=num2
        )

        if error:
            return {'message': error}, 400

        return {'result': result}, 201

@transaction_blp.route('/<int:transaction_id>')
class Transaction(MethodView):
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def delete(self, transaction_id):
        result, error = delete_transaction(transaction_id=transaction_id)

        if error:
            return {'message': error}, 400

        return {'result': result}, 200