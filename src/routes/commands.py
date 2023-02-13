from flask import Blueprint
import click

commands = Blueprint('commands', __name__)


@commands.cli.command('list-commands')
def list_commands():
    click.echo('list-users\ncreate-admin\ninit-db\ndrop-db')
