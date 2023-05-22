from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

from api.controllers.operation import get_operations,create_operation
from api.schemas.operation_schema import OperationSchema

operation_blp = Blueprint('operation', __name__, description="Operations Blueprint")

@operation_blp.route('/')
class Operation(MethodView):
    @jwt_required()
    def get(self):
        operations = get_operations()
        return operations

    @jwt_required()
    @operation_blp.arguments(OperationSchema)
    @operation_blp.response(201, OperationSchema)
    def post(self, data):
        operation = create_operation(data)
        return operation, 201