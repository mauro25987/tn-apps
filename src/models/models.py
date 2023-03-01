from flask_login import UserMixin
from werkzeug.security import check_password_hash
from utils.config import db


class User(UserMixin, db.Model):
    __bind_key__ = None

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, password, email, name, last_name, is_admin):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.last_name = last_name
        self.is_admin = is_admin

    def __repr__(self):
        return f'User: {self.username}'

    def check_password(self, password):
        return check_password_hash(self.password, password)


class AppList(UserMixin, db.Model):
    __bind_key__ = None

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(100), nullable=False)

    def __init__(self, name, logo):
        self.name = name
        self.logo = logo

    def __repr__(self):
        return f'App: {self.name}'


class AppUser(UserMixin, db.Model):
    __bind_key__ = None

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    id_app = db.Column(db.Integer, db.ForeignKey('applist.id'), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    sources = db.Column(db.String(100), nullable=False)
    campaigns = db.Column(db.String(100), nullable=False)

    def __init__(self, id_user, id_app, url, sources, campaigns):
        self.id_user = id_user
        self.id_app = id_app
        self.url = url
        self.sources = sources
        self.campaigns = campaigns

    # def __repr__(self):
    #    return f'App: {self.name}'
