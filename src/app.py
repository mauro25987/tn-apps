from flask import Flask
from utils.config import DevelopmentConfig


def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig())

    @app.route('/')
    def index():
        return 'hola mundo'

    return app
