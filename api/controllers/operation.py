from api.models import OperationModel
from api.schemas import OperationSchema
from api.utils.database import db

operation_schema = OperationSchema()


def get_operations():
    operations = OperationModel.query.all()
    return operation_schema.dumps(operations, many=True)

def get_operation(operation_id):
    operation = OperationModel.query.get(operation_id)
    if operation:
        return operation_schema.dump(operation)
    return None

def create_operation(operation_data):
    operation = OperationModel(**operation_data)
    db.session.add(operation)
    db.session.commit()
    return operation