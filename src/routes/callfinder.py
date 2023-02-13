from flask import Blueprint, render_template

callfinder = Blueprint('callfinder', __name__, url_prefix='/callfinder')


@callfinder.route('/')
def index():
    return render_template('callfinder/index.html')
