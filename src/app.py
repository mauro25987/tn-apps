from flask import Flask
from utils.config import db, migrate, config, login_manager
from routes.auth import auth as auth_blueprint
from routes.admin import admin as admin_blueprint
from routes.main import main as main_blueprint
from routes.callfinder import callfinder as callfinder_blueprint
from routes.commands import commands as commands_blueprint


def create_app(enviroment):
    app = Flask(__name__)

    # load configs class
    app.config.from_object(enviroment)

    # initialize database and migrate
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    # initialize login manager
    login_manager.init_app(app)

    # register blueprints
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(callfinder_blueprint)
    app.register_blueprint(commands_blueprint)

    return app


enviroment = config['development']
