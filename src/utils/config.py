import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
db = SQLAlchemy()

db_sqlite = os.environ['SQLITE_DB']

db_user = os.environ['VICI_MARIADB_USER']
db_db = os.environ['VICI_MARIADB_DATABASE']
db_pw = os.environ['VICI_MARIADB_PASSWORD']
db_host = os.environ['VICI_MARIADB_HOST']
db_user2 = os.environ['VICI2_MARIADB_USER']
db_db2 = os.environ['VICI2_MARIADB_DATABASE']
db_pw2 = os.environ['VICI2_MARIADB_PASSWORD']
db_host2 = os.environ['VICI2_MARIADB_HOST']


SQLITE_CONNECTION_URI = f'sqlite:///{db_sqlite}'
MYSQL_CONNECTION_URI = f'mysql+pymysql://{db_user}:{db_pw}@{db_host}/{db_db}'
MYSQL2_CONNECTION_URI = f'mysql+pymysql://{db_user}:{db_pw}@{db_host}/{db_db}'


class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = 'development'
    SECRET_KEY = 'dev'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = SQLITE_CONNECTION_URI
    SQLALCHEMY_BINDS = {
        "vicibox":  MYSQL_CONNECTION_URI,
        "vicibox2": MYSQL2_CONNECTION_URI,
    }


class ProductionConfig(Config):
    ENV = 'production'
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = SQLITE_CONNECTION_URI
    SQLALCHEMY_BINDS = {
        "vicibox":  MYSQL_CONNECTION_URI,
        "vicibox2": MYSQL2_CONNECTION_URI,
    }
