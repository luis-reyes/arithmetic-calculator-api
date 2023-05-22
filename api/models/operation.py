
from api.utils.database import db

class OperationModel(db.Model):
    __tablename__ = 'operation'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Operation id={self.id}, type={self.type}>'

    @classmethod
    def generate_default_data(cls):
        default_operations = [
            {'type': 'addition', 'cost': 1.0},
            {'type': 'subtraction', 'cost': 1.0},
            {'type': 'multiplication', 'cost': 1.5},
            {'type': 'division', 'cost': 2.0},
            {'type': 'square_root', 'cost': 2.5},
            {'type': 'random_string', 'cost': 3.0}
        ]

        for operation_data in default_operations:
            operation = cls(**operation_data)
            db.session.add(operation)

        db.session.commit()