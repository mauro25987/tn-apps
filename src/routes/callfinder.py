from flask import Blueprint, render_template, jsonify
from utils.config import db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

load_dotenv()

callfinder = Blueprint('callfinder', __name__, url_prefix='/callfinder')

ovh_data = {
    "host": os.environ['VICI_MARIADB_HOST'],
    "user": os.environ['VICI_MARIADB_USER'],
    "password": os.environ['VICI_MARIADB_PASSWORD'],
    "database": os.environ['VICI_MARIADB_USER'],
}

ovh2_data = {
    "host": os.environ['VICI2_MARIADB_HOST'],
    "user": os.environ['VICI2_MARIADB_USER'],
    "password": os.environ['VICI2_MARIADB_PASSWORD'],
    "database": os.environ['VICI2_MARIADB_USER'],
}

servers = {
    "vicidial":  ovh_data,
    "vicidial2": ovh2_data,
}


@callfinder.route('/')
def index():
    sources = get_sources()
    return render_template('callfinder/index.html', data=sources.get_json())


@callfinder.route('/api/_get_sources', methods=["GET"])
def get_sources():
    sources = list(servers)
    return jsonify(sources)


@callfinder.route('/api/_get_campaigns/<source>')
def get_campaings(source):
    Base = automap_base()
    Base.prepare(db.engines[source])
    Campaigns = Base.classes.vicidial_campaigns

    session = Session(db.get_engine(source))
    # query_result = session.execute(db.select(Campaigns)).scalars()
    query_result = session.query(Campaigns).filter(Campaigns.active == 'Y')
    result = list()

    for i in query_result:
        result.append(i.campaign_name)

    return jsonify(result)
