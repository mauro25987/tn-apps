from flask import Flask
from utils.config import DevelopmentConfig
from utils.commands import list_commands
from routes.auth import auth as auth_blueprint
from routes.main import main as main_blueprint
from routes.callfinder import callfinder as callfinder_blueprint


def create_app():
    app = Flask(__name__)

    # load configs class
    app.config.from_object(DevelopmentConfig())

    # register blueprints
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(callfinder_blueprint)

    # register commands
    app.cli.add_command(list_commands)

    return app
