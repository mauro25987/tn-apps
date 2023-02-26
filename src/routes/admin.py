from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/user/register')
def user_register():
    pass


@admin.route('/user/update/<id>')
def user_update(id):
    pass

@admin.route('/users/delete/<id>')
def user_delete(id):
    pass
