from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from models.forms import RegisterForm
from models.models import User
from utils.config import db

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('users')
def users():
    form = RegisterForm()
    list_users = User.query.all()
    return render_template('admin/users.html', users=list_users, form=form)


@admin.route('/user/register', methods=['GET', 'POST'])
def user_register():
    form = RegisterForm()

    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash(f'User {form.username.data} already exists')
        else:
            user = User(
                form.username.data,
                generate_password_hash(form.password.data, method='sha256'),
                form.email.data, form.name.data, form.last_name.data,
                form.is_admin.data
                )
            db.session.add(user)
            db.session.commit()
            flash(f'User {form.username.data} added successfully')

    if form.errors:
        flash('Error form')

    return redirect(url_for('admin.users'))


@admin.route('/user/update/<id>')
def user_update(id):
    pass


@admin.route('/users/delete/<id>')
def user_delete(id):
    pass
