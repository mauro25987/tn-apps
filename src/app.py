from flask import Flask
from utils.config import DevelopmentConfig


def create_app():
    app = Flask(__name__)

    # load configs class
    app.config.from_object(DevelopmentConfig())

    # register blueprints
    from routes.auth import auth as auth_blueprint
    from routes.main import main as main_blueprint
    from routes.callfinder import callfinder as callfinder_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(callfinder_blueprint)

    @app.route('/')
    def index():
        return 'hola mundo'

    return app
