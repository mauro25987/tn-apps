from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login')
def login():
    pass


@auth.route('/logout')
def logout():
    pass
