from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, EmailField
from wtforms.validators import InputRequired, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class RegisterForm(FlaskForm):
    username = StringField(
        'Username', validators=[InputRequired(), Length(min=3, max=50)]
        )
    password = PasswordField(
        'Password', validators=[
            InputRequired(), Length(min=6, max=50),
            EqualTo('password_confirm', message='Password incorrect')
            ]
        )
    password_confirm = PasswordField(
        'Repeat Password', validators=[InputRequired()]
        )
    email = EmailField(
        'Email', validators=[InputRequired(), Length(min=5, max=50)]
        )
    name = StringField(
        'Name', validators=[InputRequired(), Length(min=3, max=50)]
        )
    last_name = StringField('Last Name', validators=[Length(min=3, max=50)])
    is_admin = BooleanField('Admin')
