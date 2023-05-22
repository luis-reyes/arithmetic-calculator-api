from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from api.v1.resources.operation import operation_blp as OperationBlueprint
from api.v1.resources.record import transaction_blp as TransactionBlueprint
from api.v1.resources.user import user_blp as UserBlueprint
from api.utils.database import db
from api.config import config_by_name

from api.models import OperationModel

# Initialize extensions
jwt = JWTManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    api = Api(app)
    with app.app_context():
        db.create_all()
        OperationModel.generate_default_data()

        
    api.register_blueprint(OperationBlueprint, url_prefix='/api/v1/operations')
    api.register_blueprint(TransactionBlueprint, url_prefix='/api/v1/transactions')
    api.register_blueprint(UserBlueprint, url_prefix='/api/v1/users')

    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run(host='0.0.0.0', port=5000)
