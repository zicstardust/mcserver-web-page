from flask_sqlalchemy import SQLAlchemy
from lib.models import *


def create_default_database_register(database:SQLAlchemy):
    u = database.session.query(User).all()
    if not u:
        u = User(user='admin',
                 password='admin')
        database.session.add(u)
        database.session.commit()

    c = database.session.query(Craftyapi).all()
    if not c:
        c = Craftyapi(url='https://crafty.exemple.com',
                      server_id='',
                      api_key='')
        database.session.add(c)
        database.session.commit()
    
    i = database.session.query(Infos).all()
    if not i:
        i = Infos(server_java= 'play.exemple.com',
                  server_bedrock='',
                  server_map='',
                  discord_link='')
        database.session.add(i)
        database.session.commit()
