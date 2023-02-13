from flask import Flask
from utils.config import db, DevelopmentConfig
from routes.auth import auth as auth_blueprint
from routes.main import main as main_blueprint
from routes.callfinder import callfinder as callfinder_blueprint
from routes.commands import commands as commands_blueprint


def create_app():
    app = Flask(__name__)

    # load configs class
    app.config.from_object(DevelopmentConfig())

    # initialize database
    db.init_app(app)

    # register blueprints
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(callfinder_blueprint)
    app.register_blueprint(commands_blueprint)

    return app
