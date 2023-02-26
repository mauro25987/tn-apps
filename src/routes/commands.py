from flask import Blueprint
from utils.config import db
from models.models import User
import click

commands = Blueprint('commands', __name__)


@commands.cli.command('list-commands')
def list_commands():
    click.echo('list-users\ncreate-admin\ninit-db\ndrop-db')


# run the command - flask --app src/run commands init-db
@commands.cli.command('init-db')
def init_db():
    db.create_all()
    click.echo('Initialized the database.')


@commands.cli.command('create-user')
@click.argument('username')
@click.argument('password')
@click.argument('email')
@click.argument('is_admin')
def create_user(username, password, email, is_admin):
    if is_admin == 'True':
        is_admin = True
    else:
        is_admin = False
    admin = User(username, password, email, is_admin)
    db.session.add(admin)
    db.session.commit()
    click.echo(f"Usuario creado\nUsuario - {username}\nClave - {password}")
    click.echo(f"Email - {email}\nAdmin - {is_admin}")
