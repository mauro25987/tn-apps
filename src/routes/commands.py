from flask import Blueprint
from werkzeug.security import generate_password_hash
from utils.config import db
from models.models import User
import click

commands = Blueprint('commands', __name__)


# run the command - flask --app src/run commands (command)
@commands.cli.command('list-commands')
def list_commands():
    click.echo('list-users\ncreate-user\ninit-db\ndrop-db')


@commands.cli.command('list-users')
def list_users():
    users = User.query.all()
    for i in users:
        click.echo(f'{i.username} - {i.email} - {i.name} - {i.last_name} \
- {i.is_admin}')


@commands.cli.command('init-db')
def init_db():
    db.create_all()
    click.echo('Initialized the database')


@commands.cli.command('drop-db')
def drop_db():
    db.drop_all()
    click.echo('Droped the database')


@commands.cli.command('create-user')
@click.argument('username')
@click.argument('password')
@click.argument('email')
@click.argument('name')
@click.argument('last_name')
@click.argument('is_admin')
def create_user(username, password, email, name, last_name, is_admin):
    if is_admin == 'True':
        is_admin = True
    else:
        is_admin = False
    user = User(
        username, generate_password_hash(password, method="sha256"),
        email, name, last_name, is_admin
    )
    db.session.add(user)
    db.session.commit()
    click.echo(f"Usuario creado\nUsuario - {username}\nClave - {password}")
    click.echo(f"Email - {email}\nAdmin - {is_admin}")
