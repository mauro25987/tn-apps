from flask import Blueprint, redirect, render_template, flash, url_for
from flask_login import current_user, login_user, logout_user, login_required
from models.models import User
from models.forms import LoginForm
from utils.config import login_manager

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm(meta={'csrf': False})

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        #if user and user.check_password(form.password.data):
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('User or Password Incorrect')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
