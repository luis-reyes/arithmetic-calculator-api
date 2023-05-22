from datetime import datetime

from api.models import RecordModel, UserModel, OperationModel
from api.schemas import RecordSchema

from api.config import Config

from api.utils.database import db
from api.utils.random_string import get_random_string
from api.controllers.operation import get_operation


record_schema = RecordSchema()

def get_user_balance(user_id):
    # Retrieve the latest record for the user
    latest_record = RecordModel.query.filter_by(user_id=user_id).order_by(RecordModel.date.desc()).first()

    if latest_record:
        current_balance = latest_record.user_balance
    else:
        # Set a default balance if no records found
        current_balance = Config.USER_STARTING_BALANCE

    return current_balance


def calculate_operation(user_id,operation_id, num1, num2):

    user_balance = get_user_balance(user_id=user_id)
    operation = get_operation(operation_id)
    
    if not operation:
            return None,"Operation not found"

    if operation["cost"] > user_balance:
        return None, "Insufficient balance"

    if  operation["type"]== "addition":
        result = num1 + num2
    elif operation["type"] == "subtraction":
        result = num1 - num2
    elif operation["type"] == "multiplication":
        result = num1 * num2
    elif operation["type"] == "division":
        if num2 != 0:
            result = num1 / num2
        else:
            return None, "Cannot divide by zero"
    elif operation["type"]== "square_root":
        num2= ""
        if num1 >= 0:
            result = num1 ** 0.5
        else:
            return None, "Invalid input for square root"
    elif operation["type"] == "random_string":
        num1= ""
        num2= ""
        result = get_random_string()

    if not num2:
        operation_response = f"{operation['type']} {num1} equals {result}"
    else:
        operation_response = f"{operation['type']} of {num1} and {num2} equals {result}"
    

    new_record = RecordModel(
        user_id=user_id,
        operation_id=operation_id,
        amount=operation["cost"],
        user_balance=user_balance - operation["cost"],
        operation_response=operation_response,
        date=datetime.now()
    )

    db.session.add(new_record)
    db.session.commit()


    return record_schema.dump(new_record), None


def get_all_transactions(page, per_page, operation_id, user_id):
    
    
    query = db.session.query(RecordModel)
    
    if operation_id:
        query = query.filter(RecordModel.operation_id == operation_id)
    query = query.filter(RecordModel.user_id == user_id)
    query = query.filter(RecordModel.deleted == False)


    # Apply pagination
    transactions = query.paginate(page=page, per_page=per_page, error_out=False)

    
    result = {
        'transactions': [],
        'total_pages': transactions.pages,
        'total_items': transactions.total,
    }

    for transaction in transactions.items:
        transaction_data = {
            'id': transaction.id,
            'amount': transaction.amount,
            'user_balance' : transaction.user_balance,
            'operation_response' : transaction.operation_response,
            'user': {
                'id': transaction.user.id,
                'username': transaction.user.username
            },
            'operation': {
                'id': transaction.operation.id,
                'type': transaction.operation.type
            },
            'date': transaction.date
        }
        result['transactions'].append(transaction_data)

    return result,None

def delete_transaction(transaction_id):
    transaction = RecordModel.query.get(transaction_id)
    if not transaction:
        return None, {'message': 'Transaction not found'}

    transaction.soft_delete()
    return {'message': 'Transaction deleted successfully'}, None
