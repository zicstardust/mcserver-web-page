import hashlib
from flask_sqlalchemy import SQLAlchemy
from os.path import exists
from lib.models import *
from secrets import token_urlsafe

def password_to_hash(password:str):
    hash = hashlib.sha256(password.encode(encoding='utf-8'))
    return hash.hexdigest()

def get_secret_key(filename):
    if exists (filename):
        file = open(filename, "r")
        secret_key = file.read()
        file.close()
    else:
        secret_key = token_urlsafe(16)
        with open(filename, 'w') as file_object:
            print(secret_key, file=file_object)
    return secret_key

def create_default_database_register(database:SQLAlchemy):
    u = database.session.query(User).all()
    if not u:
        u = User(user='admin',
                 password=password_to_hash('admin'))
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
