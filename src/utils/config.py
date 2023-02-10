# import os
# from dotenv import load_dotenv

# load_dotenv()
# db_sqlite = os.environ['SQLITE_DB']
# SQLITE_CONNECTION_URI = f'sqlite:///{db_sqlite}'

class Config(object):
    TESTING = False


class DevelopmentConfig(Config):
    ENV = 'development'
    SECRET_KEY = 'dev'
    DEBUG = True
