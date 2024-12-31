from flask_sqlalchemy import SQLAlchemy
from lib.background_image import define_background_image
from lib.api_consumer import check_api
from lib.models import User


def create_default_user(database:SQLAlchemy, Model:User, user:str, password:str):
    u = database.session.query(Model).all()
    if not u:
        u = Model(user=user, password=password)
        database.session.add(u)
        database.session.commit()



def before_start_app():
    define_background_image()
    api_status = check_api()
    if api_status != 'Ok':
        print(f'Error in Crafty environment variables: {check_api()}')