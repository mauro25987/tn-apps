from flask import Blueprint, render_template, jsonify
from utils.config import db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import String, Column, and_, or_
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

types = {
    "all":  "ALL",
    "outbound": "Outbound",
    "inbound":  "Inbound",
}


@callfinder.route('/')
def index():
    # sources = get_sources()
    # return render_template('callfinder/callfinder.html', data=sources.get_json())
    return render_template('callfinder/test.html')


@callfinder.route('/api/_get_sources')
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
        result.append([i.campaign_id, i.campaign_name])

    return jsonify(result)


@callfinder.route('/api/_get_agents_by_campaign/<source>/<campaign>')
def get_agents(source, campaign):
    Base = automap_base()

    class UserGroups(Base):
        __tablename__ = "vicidial_user_groups"
        user_group = Column(String, primary_key=True)

    Base.prepare(db.engines[source])
    Users = Base.classes.vicidial_users

    session = Session(db.get_engine(source))

    if campaign == 'ALL':
        campaign = 'ALL-CAMPAIGNS'

    query_result = (
        session.query(Users)
        .join(UserGroups, UserGroups.user_group == Users.user_group)
        .filter(UserGroups.allowed_campaigns.like(f'%{campaign}%'))
        .order_by(Users.full_name)
    )

    result = list()
    for i in query_result:
        result.append([i.user, i.full_name])

    return jsonify(result)


@callfinder.route('api/_get_types')
def get_types():
    return jsonify(types)


@callfinder.route('api/_get_campaigns_by_type/<source>/<type>')
def get_campaigns_type(source, type):
    Base = automap_base()
    Base.prepare(db.engines[source])
    Campaigns = Base.classes.vicidial_campaigns

    session = Session(db.get_engine(source))

    query_filter = list()

    if type == 'inbound':
        query_filter.append(Campaigns.campaign_allow_inbound == 'Y')
    elif type == 'outbound':
        query_filter.append(Campaigns.campaign_allow_inbound == 'N')
    else:
        (
            query_filter.append(
                or_(Campaigns.active == 'Y', Campaigns.active == 'N'))
        )

    query_result = (
        session.query(Campaigns)
        .filter(and_(Campaigns.active == 'Y', *query_filter))
    )

    result = list()
    for i in query_result:
        result.append([i.campaign_id, i.campaign_name])

    return jsonify(result)
