import click
from flask.cli import with_appcontext


@click.command('list-commands')
@with_appcontext
def list_commands():
    click.echo('list-users\ncreate-admin\ninit-db\ndrop-db')
