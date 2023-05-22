
from api.utils.database import db

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<User id={self.id}, username={self.username}>'
