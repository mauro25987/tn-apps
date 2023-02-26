from flask_login import UserMixin
from utils.config import db


class User(UserMixin, db.Model):
    __bind_key__ = None

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    is_admin = db.Column(db.Boolean)

    def __init__(self, username, password, email, is_admin):
        self.username = username
        self.password = password
        self.email = email
        self.is_admin = is_admin

    def __repr__(self):
        return f'User: {self.name}'
