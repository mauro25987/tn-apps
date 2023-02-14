from flask import Blueprint, render_template

callfinder = Blueprint('callfinder', __name__, url_prefix='/callfinder')

ovh_data = {
    "host": "192.168.70.13",
    "user": "internalreports",
    "password": "internalreports",
    "database": "asterisk",
}

ovh2_data = {
    "host": "192.168.60.15",
    "user": "internalreports",
    "password": "internalreports",
    "database": "asterisk"
}

servers = {
    "ovh":  ovh_data,
    "ovh2": ovh2_data,
}


@callfinder.route('/')
def index():
    return render_template('callfinder/index.html')
