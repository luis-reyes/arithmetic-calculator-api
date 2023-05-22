
from api.utils.database import db

class RecordModel(db.Model):
    __tablename__ = 'record'

    id = db.Column(db.Integer, primary_key=True)
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    user_balance = db.Column(db.Float, nullable=False)
    operation_response = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    deleted = db.Column(db.Boolean, default=False)


    user = db.relationship('UserModel', backref=db.backref('record', lazy="dynamic"))
    operation = db.relationship('OperationModel')

    def soft_delete(self):
        self.deleted = True
        db.session.commit()