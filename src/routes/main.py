from flask import Blueprint
from utils.config import db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

main = Blueprint('main', __name__)


@main.route('/')
def index():
    Base = automap_base()
    Base.prepare(db.engines['vicidial'])
    Users = Base.classes.vicidial_users

    session = Session(db.get_engine('vicidial'))

    result = session.execute(db.select(Users)).scalars()
    # result2 = session.query(Users).all()

    for i in result:
        print(i.user_id, i.full_name)
    return 'hola'
